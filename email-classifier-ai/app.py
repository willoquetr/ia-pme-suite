import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from src.auth import AuthService, setup_demo_user
from src.email_classifier import EmailClassifier
from src.response_generator import ResponseGenerator
from src.database import db
from src.logger import app_logger, audit_logger
from src.config import settings
from templates import get_template, list_templates, save_template


# Configuration Streamlit
st.set_page_config(
    page_title="Email Classifier AI",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main { padding: 2rem; }
    .stButton > button { width: 100%; }
    .success-box { background-color: #d4edda; padding: 1rem; border-radius: 0.5rem; }
    .error-box { background-color: #f8d7da; padding: 1rem; border-radius: 0.5rem; }
    .info-box { background-color: #d1ecf1; padding: 1rem; border-radius: 0.5rem; }
</style>
""", unsafe_allow_html=True)


def init_session():
    """Initialiser la session."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.user_id = None
        st.session_state.username = None
        st.session_state.is_admin = False
    
    # Créer utilisateur de démo
    setup_demo_user()


def login_page():
    """Page de connexion."""
    st.title("🔐 Email Classifier AI - Login")
    
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
                
                audit_logger.info(f"User {username} logged in")
                st.success(f"✅ Bienvenue {username}!")
                st.rerun()
            else:
                st.error("❌ Identifiants incorrects")
        
        st.markdown("---")
        st.markdown("**Démo rapide**: `demo` / `demo123`")


def classifier_page():
    """Page principale de classification."""
    st.title("📧 Email Classifier AI")
    
    # Sidebar - Statistiques et configuration
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        
        # Sélection du provider LLM
        provider = st.radio(
            "Provider LLM",
            ["mistral", "ollama"],
            help="Mistral = Cloud gratuit, Ollama = Local gratuit"
        )
        
        # Afficher les stats
        stats = db.execute_query(
            "SELECT COUNT(*) as total FROM email_classifications WHERE user_id = ?",
            (st.session_state.user_id,)
        )
        
        st.markdown(f"**Emails traités**: {stats[0]['total']}")
        st.markdown(f"**Utilisateur**: {st.session_state.username}")
        
        if st.button("🚪 Déconnexion"):
            st.session_state.authenticated = False
            st.rerun()
    
    # Zone de saisie email
    col1, col2 = st.columns([2, 1])
    
    with col1:
        email_content = st.text_area(
            "📝 Collez votre email ici",
            height=250,
            placeholder="Collez le contenu de l'email à analyser..."
        )
    
    with col2:
        st.markdown("### 🎯 Actions")
        classify_btn = st.button("🔍 Classifier", use_container_width=True)
    
    # Traitement
    if classify_btn and email_content:
        with st.spinner("⏳ Analyse en cours..."):
            # Classification
            classification = EmailClassifier.classify(email_content)
            
            # Résumé
            summary = ResponseGenerator.summarize(email_content)
            
            # Réponse
            template = get_template(classification['category'])
            response = ResponseGenerator.generate(
                email_content,
                classification['category'],
                template
            )
            
            # Sauvegarder en BD
            db.execute_insert(
                """
                INSERT INTO email_classifications 
                (user_id, email_content, category, confidence, summary, generated_response, template_used)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    st.session_state.user_id,
                    email_content[:500],  # Limiter pour BD
                    classification['category'],
                    classification['confidence'],
                    summary,
                    response['response'][:500],
                    classification['category']
                )
            )
            
            audit_logger.info(f"Email classified by {st.session_state.username}: {classification['category']}")
        
        # Affichage résultats
        st.markdown("---")
        st.markdown("### 📊 Résultats")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Catégorie", classification['category'].upper())
        with col2:
            st.metric("Confiance", f"{classification['confidence']:.0%}")
        with col3:
            st.metric("Type", EmailClassifier.get_category_description(classification['category']))
        
        # Résumé
        st.markdown("### 📄 Résumé")
        st.info(summary)
        
        # Réponse suggérée
        st.markdown("### 💬 Réponse suggérée")
        response_text = response['response']
        st.text_area("Réponse", value=response_text, height=200, disabled=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📋 Copier la réponse"):
                st.code(response_text, language="text")
        with col2:
            st.download_button(
                "📥 Télécharger la réponse",
                data=response_text,
                file_name=f"response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
    
    # Historique
    st.markdown("---")
    st.markdown("### 📜 Historique")
    
    history = db.execute_query(
        """
        SELECT id, category, confidence, created_at, summary
        FROM email_classifications
        WHERE user_id = ?
        ORDER BY created_at DESC
        LIMIT 20
        """,
        (st.session_state.user_id,)
    )
    
    if history:
        df = pd.DataFrame(history)
        df['created_at'] = pd.to_datetime(df['created_at'])
        st.dataframe(df, use_container_width=True)
        
        # Export CSV
        csv = df.to_csv(index=False)
        st.download_button(
            "📥 Exporter l'historique (CSV)",
            data=csv,
            file_name=f"email_history_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    else:
        st.info("📭 Aucun email classifié pour le moment")


def admin_page():
    """Page d'administration."""
    st.title("⚙️ Administration")
    
    if not st.session_state.is_admin:
        st.error("❌ Accès réservé aux administrateurs")
        return
    
    tabs = st.tabs(["Utilisateurs", "Templates", "Logs", "Stats"])
    
    # Tab Utilisateurs
    with tabs[0]:
        st.markdown("### 👥 Gestion des utilisateurs")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Nouvel utilisateur")
            new_username = st.text_input("Nom d'utilisateur")
            new_password = st.text_input("Mot de passe", type="password")
            new_email = st.text_input("Email")
            new_company = st.text_input("Entreprise")
            
            if st.button("➕ Créer utilisateur"):
                if new_username and new_password and new_email:
                    try:
                        password_hash = AuthService.hash_password(new_password)
                        db.execute_insert(
                            """
                            INSERT INTO users (username, password_hash, email, company_name)
                            VALUES (?, ?, ?, ?)
                            """,
                            (new_username, password_hash, new_email, new_company)
                        )
                        st.success(f"✅ Utilisateur {new_username} créé")
                    except Exception as e:
                        st.error(f"❌ Erreur: {e}")
        
        with col2:
            st.markdown("#### Utilisateurs existants")
            users = db.execute_query("SELECT id, username, email, company_name, created_at FROM users")
            if users:
                df = pd.DataFrame(users)
                st.dataframe(df, use_container_width=True)
    
    # Tab Templates
    with tabs[1]:
        st.markdown("### 📋 Gestion des templates")
        
        category = st.selectbox("Catégorie", EmailClassifier.get_categories())
        templates = list_templates(category)
        
        st.markdown(f"**Templates pour {category}**: {', '.join(templates)}")
        
        template_name = st.text_input("Nom du template", value="custom")
        template_content = st.text_area(
            "Contenu du template",
            height=200,
            value=get_template(category)
        )
        
        if st.button("💾 Sauvegarder le template"):
            save_template(category, template_name, template_content)
            st.success(f"✅ Template {template_name} sauvegardé")
    
    # Tab Logs
    with tabs[2]:
        st.markdown("### 📋 Logs d'audit")
        
        logs = db.execute_query("""
            SELECT u.username, a.action, a.details, a.created_at
            FROM audit_logs a
            LEFT JOIN users u ON a.user_id = u.id
            ORDER BY a.created_at DESC
            LIMIT 100
        """)
        
        if logs:
            df = pd.DataFrame(logs)
            st.dataframe(df, use_container_width=True)
    
    # Tab Stats
    with tabs[3]:
        st.markdown("### 📊 Statistiques")
        
        col1, col2, col3 = st.columns(3)
        
        stats = db.execute_query("SELECT COUNT(*) as count FROM users")
        with col1:
            st.metric("Total utilisateurs", stats[0]['count'])
        
        stats = db.execute_query("SELECT COUNT(*) as count FROM email_classifications")
        with col2:
            st.metric("Total emails classifiés", stats[0]['count'])
        
        categories = db.execute_query("""
            SELECT category, COUNT(*) as count
            FROM email_classifications
            GROUP BY category
            ORDER BY count DESC
        """)
        
        with col3:
            if categories:
                df = pd.DataFrame(categories)
                st.bar_chart(data=df.set_index("category"))


def main():
    """Point d'entrée principal."""
    init_session()
    
    if not st.session_state.authenticated:
        login_page()
    else:
        # Menu de navigation
        page = st.sidebar.radio("Navigation", ["Classifier", "Admin"])
        
        if page == "Classifier":
            classifier_page()
        else:
            admin_page()


if __name__ == "__main__":
    main()
