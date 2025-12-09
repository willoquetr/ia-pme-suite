import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from src.auth import AuthService, setup_demo_user
from src.excel_analyzer import ExcelAnalyzer
from src.database import db
from src.logger import app_logger, audit_logger
from src.config import settings


st.set_page_config(
    page_title="Excel Analyzer AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


def init_session():
    """Initialiser la session."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.user_id = None
        st.session_state.username = None
        st.session_state.is_admin = False
    
    setup_demo_user()


def login_page():
    """Page de connexion."""
    st.title("🔐 Excel Analyzer AI - Login")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Connexion utilisateur")
        
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        
        if st.button("🔓 Se connecter", use_container_width=True):
            users = db.execute_query(
                "SELECT * FROM users WHERE username = ?",
                (username,)
            )
            
            if users and AuthService.verify_password(password, users[0]['password_hash']):
                user = users[0]
                st.session_state.authenticated = True
                st.session_state.user_id = user['id']
                st.session_state.username = user['username']
                st.session_state.is_admin = user['is_admin']
                
                audit_logger.info(f"User {username} logged in (Excel Analyzer)")
                st.success(f"✅ Bienvenue {username}!")
                st.rerun()
            else:
                st.error("❌ Identifiants incorrects")
        
        st.markdown("---")
        st.markdown("**Démo rapide**: `demo` / `demo123`")


def analyzer_page():
    """Page principale."""
    st.title("📊 Excel Analyzer AI")
    
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        st.markdown(f"**Utilisateur**: {st.session_state.username}")
        
        if st.button("🚪 Déconnexion"):
            st.session_state.authenticated = False
            st.rerun()
    
    # Upload du fichier
    st.markdown("### 📤 Upload un fichier Excel")
    uploaded_file = st.file_uploader(
        "Sélectionnez un fichier Excel ou CSV",
        type=["xlsx", "xls", "csv"],
        help=f"Max {settings.max_file_size_mb}MB"
    )
    
    if uploaded_file:
        # Lire le contenu
        file_content = uploaded_file.read()
        file_name = uploaded_file.name
        file_size_mb = len(file_content) / (1024**2)
        
        if file_size_mb > settings.max_file_size_mb:
            st.error(f"❌ File too large (max {settings.max_file_size_mb}MB)")
        else:
            st.success(f"✅ File loaded ({file_size_mb:.2f}MB)")
            
            # Parser
            with st.spinner("⏳ Parsing file..."):
                success, message, data = ExcelAnalyzer.parse_file(file_content, file_name)
            
            if not success:
                st.error(f"❌ {message}")
            else:
                st.success(message)
                
                # Analyser
                with st.spinner("🔍 Analyzing..."):
                    analysis = ExcelAnalyzer.analyze(data)
                
                # Sauvegarder en BD
                try:
                    db.execute_insert(
                        """
                        INSERT INTO analyses 
                        (user_id, file_name, summary, anomalies, suggestions, status)
                        VALUES (?, ?, ?, ?, ?, ?)
                        """,
                        (
                            st.session_state.user_id,
                            file_name,
                            str(analysis['summary']),
                            str(analysis['anomalies']),
                            str(analysis['suggestions']),
                            "completed"
                        )
                    )
                    audit_logger.info(f"File analyzed by {st.session_state.username}: {file_name}")
                except:
                    pass
                
                # Afficher les résultats
                st.markdown("---")
                st.markdown("### 📈 Résultats d'analyse")
                
                tabs = st.tabs(["Summary", "Anomalies", "Statistics", "Suggestions"])
                
                # Tab Summary
                with tabs[0]:
                    for sheet_name, summary in analysis['summary'].items():
                        st.markdown(f"**Sheet: {sheet_name}**")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Rows", summary['rows'])
                        with col2:
                            st.metric("Columns", summary['columns'])
                        with col3:
                            st.metric("Size (MB)", f"{summary['memory_usage_mb']:.2f}")
                
                # Tab Anomalies
                with tabs[1]:
                    if analysis['anomalies']:
                        anomaly_df = pd.DataFrame(analysis['anomalies'])
                        st.dataframe(anomaly_df, use_container_width=True)
                        
                        # Visualisation
                        if len(anomaly_df) > 0:
                            severity_counts = anomaly_df['severity'].value_counts()
                            fig = px.bar(
                                severity_counts,
                                title="Anomalies by Severity",
                                labels={"index": "Severity", "value": "Count"}
                            )
                            st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.success("✅ No anomalies detected!")
                
                # Tab Statistics
                with tabs[2]:
                    for sheet_name, stats in analysis['statistics'].items():
                        st.markdown(f"**Sheet: {sheet_name}**")
                        if 'numeric_cols' in stats:
                            stats_df = pd.DataFrame(stats['numeric_cols']).T
                            st.dataframe(stats_df, use_container_width=True)
                
                # Tab Suggestions
                with tabs[3]:
                    if analysis['suggestions']:
                        for suggestion in analysis['suggestions']:
                            st.info(f"💡 {suggestion}")
                    else:
                        st.success("✅ No suggestions!")
    
    # Historique
    st.markdown("---")
    st.markdown("### 📜 Historique des analyses")
    
    history = db.execute_query(
        """
        SELECT id, file_name, created_at
        FROM analyses
        WHERE user_id = ?
        ORDER BY created_at DESC
        LIMIT 10
        """,
        (st.session_state.user_id,)
    )
    
    if history:
        df = pd.DataFrame(history)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("📭 No analyses yet")


def main():
    """Point d'entrée."""
    init_session()
    
    if not st.session_state.authenticated:
        login_page()
    else:
        analyzer_page()


if __name__ == "__main__":
    main()
