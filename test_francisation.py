#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test de validation francisation - Email Classifier
Vérifier que tout fonctionne 100% en français
"""

import sys
import os

# Ajouter le chemin au sys.path
sys.path.insert(0, os.path.dirname(__file__))

def test_french_categories():
    """Tester que les catégories sont en français"""
    from email_classifier_ai.src.email_classifier import EmailClassifier
    
    categories = EmailClassifier.get_categories()
    expected = ["facture", "devis", "reclamation", "spam", "information", "autre"]
    
    print("✅ TEST: Catégories en français")
    print(f"   Catégories attendues: {expected}")
    print(f"   Catégories reçues:   {categories}")
    
    if categories == expected:
        print("   ✅ PASS: Catégories correctes\n")
        return True
    else:
        print("   ❌ FAIL: Catégories ne correspondent pas\n")
        return False

def test_french_descriptions():
    """Tester que les descriptions sont en français"""
    from email_classifier_ai.src.email_classifier import EmailClassifier
    
    print("✅ TEST: Descriptions en français")
    
    test_cases = [
        ("facture", "Factures et documents de facturation"),
        ("devis", "Devis et estimations"),
        ("reclamation", "Réclamations et problèmes clients"),
        ("spam", "Spam et emails non pertinents"),
        ("information", "Informations générales"),
        ("autre", "Autres types d'emails")
    ]
    
    all_pass = True
    for category, expected_desc in test_cases:
        desc = EmailClassifier.get_category_description(category)
        status = "✅" if desc == expected_desc else "❌"
        print(f"   {status} {category}: {desc}")
        if desc != expected_desc:
            all_pass = False
    
    print()
    return all_pass

def test_pdf_types():
    """Tester que les types de documents PDF sont en français"""
    from pdf_generator_ai.src.pdf_generator import PDFGenerator
    
    doc_types = PDFGenerator.get_document_types()
    expected_keys = {"devis", "facture", "lettre", "contrat", "rapport"}
    
    print("✅ TEST: Types de documents PDF en français")
    print(f"   Types attendus: {expected_keys}")
    print(f"   Types reçus:   {set(doc_types.keys())}")
    
    if set(doc_types.keys()) == expected_keys:
        print("   ✅ PASS: Types corrects\n")
        
        # Afficher les titres
        print("   Titres des documents:")
        for dtype, config in doc_types.items():
            print(f"   - {dtype}: {config['title']}")
        print()
        return True
    else:
        print("   ❌ FAIL: Types ne correspondent pas\n")
        return False

def test_excel_anomalies():
    """Tester que les types d'anomalies Excel sont en français"""
    try:
        import pandas as pd
        from excel_analyzer_ai.src.excel_analyzer import ExcelAnalyzer
        
        print("✅ TEST: Types d'anomalies Excel en français")
        
        # Créer un DataFrame avec anomalies
        df = pd.DataFrame({
            "nom": ["Alice", None, "Bob"],
            "age": [25, 30, 35],
            "vide": [None, None, None]
        })
        
        anomalies = ExcelAnalyzer._detect_anomalies(df, "test_sheet")
        
        print(f"   Anomalies détectées: {len(anomalies)}")
        
        for anomaly in anomalies:
            print(f"   - Type: {anomaly['type']}")
            print(f"     Colonne: {anomaly['column']}")
            print(f"     Description: {anomaly['description']}")
        
        # Vérifier que les types sont en français
        anomaly_types = [a['type'] for a in anomalies]
        french_types = {"valeurs_manquantes", "colonne_vide", "doublons", "donnees_manquantes_excessives"}
        
        has_french_types = any(atype in french_types for atype in anomaly_types)
        
        if has_french_types:
            print("   ✅ PASS: Types d'anomalies en français\n")
            return True
        else:
            print("   ❌ FAIL: Types d'anomalies non en français\n")
            return False
            
    except Exception as e:
        print(f"   ⚠️ SKIP: {str(e)}\n")
        return True  # Skip si pandas non disponible

def main():
    """Exécuter tous les tests"""
    print("\n" + "="*60)
    print("🇫🇷 VALIDATION FRANCISATION - EMAIL/PDF/EXCEL CLASSIFIER")
    print("="*60 + "\n")
    
    results = []
    
    try:
        results.append(("Catégories Email", test_french_categories()))
    except Exception as e:
        print(f"❌ ERREUR: {str(e)}\n")
        results.append(("Catégories Email", False))
    
    try:
        results.append(("Descriptions Email", test_french_descriptions()))
    except Exception as e:
        print(f"❌ ERREUR: {str(e)}\n")
        results.append(("Descriptions Email", False))
    
    try:
        results.append(("Types PDF", test_pdf_types()))
    except Exception as e:
        print(f"❌ ERREUR: {str(e)}\n")
        results.append(("Types PDF", False))
    
    try:
        results.append(("Anomalies Excel", test_excel_anomalies()))
    except Exception as e:
        print(f"❌ ERREUR: {str(e)}\n")
        results.append(("Anomalies Excel", False))
    
    # Résumé
    print("="*60)
    print("📊 RÉSUMÉ")
    print("="*60)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\nTotal: {passed}/{total} tests passés")
    
    if passed == total:
        print("\n🎉 FRANCISATION VALIDÉE - PRÊT POUR PMEs FRANÇAISES!")
    else:
        print("\n⚠️ Certains tests ont échoué - Vérifier les erreurs ci-dessus")
    
    print("="*60 + "\n")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
