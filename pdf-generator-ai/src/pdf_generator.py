import os
from datetime import datetime
from typing import Dict, Optional
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from src.config import settings
from src.logger import app_logger
from src.llm_service import LLMService


class PDFGenerator:
    """Service de génération PDF."""
    
    DOCUMENT_TYPES = {
        "devis": {
            "title": "Devis",
            "fields": ["nom_client", "email_client", "description", "montant", "validite_jours"],
            "description": "Devis professionnel pour services ou produits"
        },
        "facture": {
            "title": "Facture",
            "fields": ["nom_client", "numero_facture", "description", "montant", "date_echéance"],
            "description": "Facture pour paiement"
        },
        "lettre": {
            "title": "Lettre commerciale",
            "fields": ["nom_destinataire", "sujet", "corps", "nom_signature"],
            "description": "Lettre commerciale professionnelle"
        },
        "contrat": {
            "title": "Contrat",
            "fields": ["partie_a", "partie_b", "sujet", "conditions", "date_effective"],
            "description": "Contrat de service simple"
        },
        "rapport": {
            "title": "Rapport",
            "fields": ["titre_rapport", "date", "résumé", "conclusions", "recommandations"],
            "description": "Rapport professionnel"
        }
    }
    
    @staticmethod
    def get_document_types() -> Dict:
        """Obtenir les types de documents disponibles."""
        return PDFGenerator.DOCUMENT_TYPES
    
    @staticmethod
    def get_required_fields(doc_type: str) -> list:
        """Obtenir les champs requis pour un type de document."""
        if doc_type in PDFGenerator.DOCUMENT_TYPES:
            return PDFGenerator.DOCUMENT_TYPES[doc_type]["fields"]
        return []
    
    @staticmethod
    def validate_fields(doc_type: str, fields: Dict) -> tuple[bool, str]:
        """Valider les champs pour un type de document."""
        # Vérifier que le type existe
        if doc_type not in PDFGenerator.DOCUMENT_TYPES:
            return False, f"Type de document inconnu: {doc_type}"

        required_fields = PDFGenerator.get_required_fields(doc_type)
        missing_fields = [f for f in required_fields if f not in fields or not fields[f]]

        if missing_fields:
            return False, f"Champs manquants: {', '.join(missing_fields)}"

        return True, "OK"
    
    @staticmethod
    def generate_pdf(
        doc_type: str,
        fields: Dict,
        output_path: Optional[str] = None,
        use_ai: bool = True
    ) -> tuple[bool, str, Optional[str]]:
        """
        Générer un PDF.
        
        Args:
            doc_type: Type de document (quote, invoice, etc.)
            fields: Dictionnaire des champs
            output_path: Chemin de sortie (optionnel)
            use_ai: Utiliser l'IA pour générer le contenu
            
        Returns:
            (success, message, pdf_path)
        """
        try:
            # Normaliser certains alias anglais courants
            type_map = {"quote": "devis", "invoice": "facture", "letter": "lettre"}
            doc_type = type_map.get(doc_type, doc_type)

            # Valider les champs
            is_valid, validation_msg = PDFGenerator.validate_fields(doc_type, fields)
            if not is_valid:
                return False, validation_msg, None
            
            # Créer dossier de sortie
            os.makedirs(settings.pdf_output_dir, exist_ok=True)
            
            # Chemin de sortie
            if not output_path:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = os.path.join(
                    settings.pdf_output_dir,
                    f"{doc_type}_{timestamp}.pdf"
                )
            
            # Générer le contenu avec l'IA si demandé (fallback fiable)
            if use_ai:
                gen = getattr(LLMService, "generate_document_content", None)
                if callable(gen):
                    try:
                        content = gen(doc_type, fields)
                    except Exception as e:
                        app_logger.error(f"LLM generate_document_content error: {e}")
                        content = PDFGenerator._generate_default_content(doc_type, fields)
                else:
                    # Provider n'implémente pas la génération de document: fallback
                    app_logger.info("LLMService.generate_document_content not available, using default content")
                    content = PDFGenerator._generate_default_content(doc_type, fields)
            else:
                content = PDFGenerator._generate_default_content(doc_type, fields)
            
            # Créer le PDF
            doc = SimpleDocTemplate(output_path, pagesize=letter)
            story = []
            
            # Styles
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor('#1f4788'),
                spaceAfter=30,
                alignment=1  # Center
            )
            
            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=14,
                textColor=colors.HexColor('#1f4788'),
                spaceAfter=12
            )
            
            # Titre
            title = PDFGenerator.DOCUMENT_TYPES[doc_type]["title"]
            story.append(Paragraph(title, title_style))
            story.append(Spacer(1, 0.2*inch))
            
            # Infos de base
            info_data = []
            for key, value in list(fields.items())[:4]:
                info_data.append([key.replace('_', ' ').title(), str(value)])
            
            if info_data:
                info_table = Table(info_data, colWidths=[2*inch, 3*inch])
                info_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f0f0f0')),
                    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, -1), 11),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                ]))
                story.append(info_table)
                story.append(Spacer(1, 0.3*inch))
            
            # Contenu
            story.append(Paragraph("Content", heading_style))
            story.append(Paragraph(content.replace('\n', '<br/>'), styles['BodyText']))
            story.append(Spacer(1, 0.5*inch))
            
            # Pied de page
            footer_data = [
                [settings.company_name, datetime.now().strftime("%Y-%m-%d")],
            ]
            footer_table = Table(footer_data, colWidths=[3*inch, 2*inch])
            footer_table.setStyle(TableStyle([
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#666666')),
                ('FONTSIZE', (0, 0), (-1, -1), 9),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
            ]))
            story.append(footer_table)
            
            # Générer le PDF
            doc.build(story)
            
            # Obtenir la taille du fichier
            file_size = os.path.getsize(output_path)
            
            app_logger.info(f"PDF generated: {output_path} ({file_size} bytes)")
            return True, "PDF generated successfully", output_path
            
        except Exception as e:
            app_logger.error(f"PDF generation error: {e}")
            return False, f"PDF generation error: {str(e)}", None
    
    @staticmethod
    def _generate_default_content(doc_type: str, fields: Dict) -> str:
        """Générer un contenu par défaut sans IA.

        Supporte les types français ('devis','facture','lettre','contrat','rapport')
        et quelques alias anglais ('quote','invoice','letter').
        """
        # Supporter les types français et quelques alias anglais
        if doc_type in ("devis", "quote"):
            return f"""
Devis pour: {fields.get('nom_client', fields.get('client_name', 'N/A'))}

Description:
{fields.get('description', 'Description du service')}

Montant: {fields.get('montant', fields.get('amount', '0.00'))}
Validité: {fields.get('validite_jours', fields.get('validity_days', '30'))} jours

Merci de confirmer si vous souhaitez procéder.
            """.strip()

        elif doc_type in ("facture", "invoice"):
            return f"""
Facture #{fields.get('numero_facture', fields.get('invoice_number', 'N/A'))}

À: {fields.get('nom_client', fields.get('client_name', 'N/A'))}

Description:
{fields.get('description', 'Services fournis')}

Montant total: {fields.get('montant', fields.get('amount', '0.00'))}
Date d'échéance: {fields.get('date_echéance', fields.get('due_date', 'À réception'))}

Merci de régler avant la date d'échéance.
            """.strip()

        elif doc_type in ("lettre", "letter"):
            return f"""
À: {fields.get('nom_destinataire', fields.get('recipient_name', 'Destinataire'))}

Sujet: {fields.get('sujet', fields.get('subject', 'Sujet'))}

Bonjour {fields.get('nom_destinataire', fields.get('recipient_name', 'Destinataire'))},

{fields.get('corps', fields.get('body', 'Corps du message'))}

Cordialement,
{fields.get('nom_signature', fields.get('signature_name', 'Expéditeur'))}
            """.strip()

        elif doc_type == "contrat":
            return f"Contrat entre {fields.get('partie_a', 'A')} et {fields.get('partie_b', 'B')}\nSujet: {fields.get('sujet', '')}".strip()

        elif doc_type == "rapport":
            return f"Rapport: {fields.get('titre_rapport', 'Titre')}\nRésumé: {fields.get('résumé', '')}".strip()

        else:
            return "Contenu par défaut pour " + doc_type
