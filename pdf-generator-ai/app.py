import streamlit as st
import pandas as pd
from datetime import datetime
from src.auth import AuthService, setup_demo_user
from src.pdf_generator import PDFGenerator
from src.database import db
from src.logger import app_logger, audit_logger
from src.config import settings


st.set_page_config(
    page_title="PDF Generator AI",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main { padding: 2rem; }
    .stButton > button { width: 100%; }
    .success-box { background-color: #d4edda; padding: 1rem; border-radius: 0.5rem; }
    .error-box { background-color: #f8d7da; padding: 1rem; border-radius: 0.5rem; }
</style>
""", unsafe_allow_html=True)


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
    st.title("🔐 PDF Generator AI - Login")
    
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
                
                audit_logger.info(f"User {username} logged in (PDF Generator)")
                st.success(f"✅ Bienvenue {username}!")
                st.rerun()
            else:
                st.error("❌ Identifiants incorrects")
        
        st.markdown("---")
        st.markdown("**Démo rapide**: `demo` / `demo123`")


def generator_page():
    """Page principale de génération PDF."""
    st.title("📄 PDF Generator AI")
    
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        st.markdown(f"**Utilisateur**: {st.session_state.username}")
        
        if st.button("🚪 Déconnexion"):
            st.session_state.authenticated = False
            st.rerun()
    
    # Sélection du type de document
    doc_types = PDFGenerator.get_document_types()
    selected_type = st.selectbox(
        "📋 Type de document",
        list(doc_types.keys()),
        format_func=lambda x: f"{doc_types[x]['title']} - {doc_types[x]['description']}"
    )
    
    # Afficher la description
    doc_info = doc_types[selected_type]
    st.info(f"**{doc_info['title']}**: {doc_info['description']}")
    
    # Formulaire dynamique pour les champs
    st.markdown("### 📝 Remplissez les informations")
    
    fields = {}
    required_fields = PDFGenerator.get_required_fields(selected_type)
    
    cols = st.columns(2)
    for idx, field in enumerate(required_fields):
        col = cols[idx % 2]
        with col:
            label = field.replace('_', ' ').title()
            
            if 'date' in field.lower():
                fields[field] = st.date_input(label)
            elif 'amount' in field.lower() or 'price' in field.lower():
                fields[field] = st.number_input(label, min_value=0.0, step=100.0)
            elif 'days' in field.lower() or 'number' in field.lower():
                fields[field] = st.number_input(label, min_value=1)
            else:
                fields[field] = st.text_input(label)
    
    # Options avancées
    with st.expander("⚙️ Options avancées"):
        use_ai = st.checkbox("Utiliser l'IA pour générer le contenu", value=True)
        custom_company = st.text_input(
            "Nom de l'entreprise (optionnel)",
            value=settings.company_name
        )
    
    # Bouton de génération
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔧 Générer le PDF", use_container_width=True):
            with st.spinner("⏳ Génération en cours..."):
                # Valider
                is_valid, msg = PDFGenerator.validate_fields(selected_type, fields)
                
                if not is_valid:
                    st.error(f"❌ {msg}")
                else:
                    # Générer
                    success, message, pdf_path = PDFGenerator.generate_pdf(
                        selected_type,
                        fields,
                        use_ai=use_ai
                    )
                    
                    if success:
                        st.success(f"✅ {message}")
                        
                        # Sauvegarder en BD
                        try:
                            file_size = None
                            if pdf_path:
                                import os
                                file_size = os.path.getsize(pdf_path)
                            
                            db.execute_insert(
                                """
                                INSERT INTO generated_documents 
                                (user_id, document_type, title, content, pdf_path, file_size, status)
                                VALUES (?, ?, ?, ?, ?, ?, ?)
                                """,
                                (
                                    st.session_state.user_id,
                                    selected_type,
                                    f"{selected_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                                    str(fields),
                                    pdf_path,
                                    file_size,
                                    "completed"
                                )
                            )
                            
                            audit_logger.info(
                                f"PDF generated by {st.session_state.username}: {selected_type}"
                            )
                        except Exception as e:
                            app_logger.error(f"Database error: {e}")
                        
                        # Bouton de téléchargement
                        if pdf_path:
                            with open(pdf_path, "rb") as f:
                                st.download_button(
                                    "📥 Télécharger le PDF",
                                    data=f.read(),
                                    file_name=f"{selected_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                                    mime="application/pdf",
                                    use_container_width=True
                                )
                    else:
                        st.error(f"❌ Erreur: {message}")
    
    with col2:
        if st.button("🔍 Aperçu", use_container_width=True):
            st.info("Aperçu du contenu généré (aperçu complet disponible après génération)")
    
    # Historique
    st.markdown("---")
    st.markdown("### 📜 Historique des documents")
    
    history = db.execute_query(
        """
        SELECT id, document_type, title, file_size, created_at
        FROM generated_documents
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
        
        csv = df.to_csv(index=False)
        st.download_button(
            "📥 Exporter l'historique (CSV)",
            data=csv,
            file_name=f"pdf_history_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    else:
        st.info("📭 Aucun document généré pour le moment")


def main():
    """Point d'entrée."""
    init_session()
    
    if not st.session_state.authenticated:
        login_page()
    else:
        generator_page()


if __name__ == "__main__":
    main()
