"""
Simple Flask API pour les démos interactives LIVE
Permet aux clients de tester les 3 apps en ligne
"""

from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
import sys
import os
from pathlib import Path

# Ajouter les chemins des apps
sys.path.insert(0, str(Path(__file__).parent / 'email-classifier-ai' / 'src'))
sys.path.insert(0, str(Path(__file__).parent / 'pdf-generator-ai' / 'src'))
sys.path.insert(0, str(Path(__file__).parent / 'excel-analyzer-ai' / 'src'))

app = Flask(__name__)
CORS(app)

# Import des services
try:
    from email_classifier import EmailClassifier
    email_classifier_available = True
except:
    email_classifier_available = False
    print("⚠️ Email Classifier not available")

try:
    from pdf_generator import PDFGenerator
    pdf_generator_available = True
except:
    pdf_generator_available = False
    print("⚠️ PDF Generator not available")

try:
    from excel_analyzer import ExcelAnalyzer
    excel_analyzer_available = True
except:
    excel_analyzer_available = False
    print("⚠️ Excel Analyzer not available")


@app.route('/')
def home():
    """Landing page - redirection vers demos.html"""
    return jsonify({
        "message": "Bienvenue sur l'API des Démos IA PME",
        "endpoints": {
            "email_classify": "/api/email/classify (POST)",
            "pdf_generate": "/api/pdf/generate (POST)",
            "excel_analyze": "/api/excel/analyze (POST)",
            "health": "/api/health (GET)"
        }
    })


@app.route('/api/health', methods=['GET'])
def health():
    """Health check - vérifie la disponibilité des services"""
    return jsonify({
        "status": "ok",
        "services": {
            "email_classifier": "available" if email_classifier_available else "unavailable",
            "pdf_generator": "available" if pdf_generator_available else "unavailable",
            "excel_analyzer": "available" if excel_analyzer_available else "unavailable"
        }
    })


@app.route('/api/email/classify', methods=['POST'])
def classify_email():
    """Classifier un email"""
    if not email_classifier_available:
        return jsonify({"error": "Email Classifier not available"}), 503
    
    try:
        data = request.json
        email_content = data.get('content', '')
        
        if not email_content:
            return jsonify({"error": "Email content is required"}), 400
        
        result = EmailClassifier.classify(email_content)
        return jsonify({
            "status": "success",
            "result": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e)
        }), 500


@app.route('/api/pdf/generate', methods=['POST'])
def generate_pdf():
    """Générer un PDF"""
    if not pdf_generator_available:
        return jsonify({"error": "PDF Generator not available"}), 503
    
    try:
        data = request.json
        doc_type = data.get('type', 'devis')
        fields = data.get('fields', {})
        
        # Validation simple
        if not fields:
            return jsonify({"error": "Fields are required"}), 400
        
        # Pour la démo, on retourne juste un aperçu (pas le vrai PDF)
        return jsonify({
            "status": "success",
            "message": "PDF généré avec succès",
            "type": doc_type,
            "fields": fields,
            "note": "Version démo - pour télécharger le vrai PDF, utiliser l'app locale"
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e)
        }), 500


@app.route('/api/excel/analyze', methods=['POST'])
def analyze_excel():
    """Analyser un fichier Excel/CSV"""
    if not excel_analyzer_available:
        return jsonify({"error": "Excel Analyzer not available"}), 503
    
    try:
        data = request.json
        csv_content = data.get('content', '')
        
        if not csv_content:
            return jsonify({"error": "CSV content is required"}), 400
        
        # Parse simple du CSV
        lines = csv_content.strip().split('\n')
        if not lines:
            return jsonify({"error": "Invalid CSV format"}), 400
        
        # Analyse basique
        analysis = {
            "rows": len(lines) - 1,  # Exclure header
            "columns": len(lines[0].split(',')),
            "issues": []
        }
        
        # Détecter les problèmes simples
        for i, line in enumerate(lines[1:], 1):
            cols = line.split(',')
            if '' in cols:
                analysis["issues"].append(f"Ligne {i}: valeur manquante détectée")
        
        return jsonify({
            "status": "success",
            "analysis": analysis
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e)
        }), 500


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    print("🚀 Demo API Server Starting...")
    print("📊 Email Classifier:", "✅" if email_classifier_available else "❌")
    print("📄 PDF Generator:", "✅" if pdf_generator_available else "❌")
    print("📈 Excel Analyzer:", "✅" if excel_analyzer_available else "❌")
    print("\n🌐 Open http://localhost:5000 to access the API")
    app.run(debug=True, host='0.0.0.0', port=5000)
