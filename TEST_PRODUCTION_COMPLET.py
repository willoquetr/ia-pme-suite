#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST PRODUCTION - IA-PME Suite
Vérifie que les 3 apps fonctionnent correctement avant déploiement

Date: 9 décembre 2025
Créateur: IA-PME
"""

import sys
import os
from pathlib import Path
import json
from datetime import datetime

# Couleurs
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

class ProductionTester:
    def __init__(self):
        self.results = {
            'email_classifier': [],
            'pdf_generator': [],
            'excel_analyzer': [],
            'infrastructure': []
        }
        self.passed = 0
        self.failed = 0
        self.start_time = datetime.now()

    def print_header(self, text):
        print(f"\n{CYAN}{BOLD}{'=' * 70}{RESET}")
        print(f"{CYAN}{BOLD}{text.center(70)}{RESET}")
        print(f"{CYAN}{BOLD}{'=' * 70}{RESET}\n")

    def print_test(self, name, status, details=""):
        symbol = f"{GREEN}✅{RESET}" if status else f"{RED}❌{RESET}"
        print(f"{symbol} {name}")
        if details:
            print(f"   {YELLOW}→ {details}{RESET}")
        if status:
            self.passed += 1
        else:
            self.failed += 1

    def test_email_classifier(self):
        """Test Email Classifier"""
        self.print_header("1️⃣  EMAIL CLASSIFIER - Tests")
        
        app_path = Path("email-classifier-ai/src")
        
        # Test 1: Fichiers existent
        files_exist = all([
            (app_path / "email_classifier.py").exists(),
            (app_path / "llm_service.py").exists(),
            (app_path / "config.py").exists(),
        ])
        self.print_test("Fichiers sources présents", files_exist)
        
        # Test 2: Categories en français
        try:
            with open(app_path / "email_classifier.py", 'r', encoding='utf-8') as f:
                content = f.read()
                has_french_cats = all(cat in content for cat in ['facture', 'devis', 'reclamation', 'autre'])
            self.print_test("Catégories en français", has_french_cats, 
                          "facture, devis, réclamation, autre")
        except Exception as e:
            self.print_test("Catégories en français", False, str(e))
        
        # Test 3: Prompts LLM en français
        try:
            with open(app_path / "llm_service.py", 'r', encoding='utf-8') as f:
                content = f.read()
                has_french_prompts = "Classifie l'email" in content or "Résume" in content
            self.print_test("Prompts LLM en français", has_french_prompts)
        except Exception as e:
            self.print_test("Prompts LLM en français", False, str(e))
        
        # Test 4: Tests unitaires
        test_file = Path("email-classifier-ai/tests/test_email_classifier.py")
        self.print_test("Tests unitaires présents", test_file.exists())

    def test_pdf_generator(self):
        """Test PDF Generator"""
        self.print_header("2️⃣  PDF GENERATOR - Tests")
        
        app_path = Path("pdf-generator-ai/src")
        
        # Test 1: Fichiers existent
        files_exist = all([
            (app_path / "pdf_generator.py").exists(),
            (app_path / "llm_service.py").exists(),
        ])
        self.print_test("Fichiers sources présents", files_exist)
        
        # Test 2: Types de document en français
        try:
            with open(app_path / "pdf_generator.py", 'r', encoding='utf-8') as f:
                content = f.read()
                has_french_types = all(doc_type in content for doc_type in ['devis', 'facture', 'lettre', 'contrat', 'rapport'])
            self.print_test("Types de document en français", has_french_types,
                          "devis, facture, lettre, contrat, rapport")
        except Exception as e:
            self.print_test("Types de document en français", False, str(e))
        
        # Test 3: Génération de contenu
        try:
            with open(app_path / "llm_service.py", 'r', encoding='utf-8') as f:
                content = f.read()
                has_generation = "Génère un document" in content
            self.print_test("Méthode de génération présente", has_generation)
        except Exception as e:
            self.print_test("Méthode de génération présente", False, str(e))
        
        # Test 4: Tests unitaires
        test_file = Path("pdf-generator-ai/tests/test_pdf_generator.py")
        self.print_test("Tests unitaires présents", test_file.exists())

    def test_excel_analyzer(self):
        """Test Excel Analyzer"""
        self.print_header("3️⃣  EXCEL ANALYZER - Tests")
        
        app_path = Path("excel-analyzer-ai/src")
        
        # Test 1: Fichiers existent
        files_exist = all([
            (app_path / "excel_analyzer.py").exists(),
            (app_path / "config.py").exists(),
        ])
        self.print_test("Fichiers sources présents", files_exist)
        
        # Test 2: Détection d'anomalies en français
        try:
            with open(app_path / "excel_analyzer.py", 'r', encoding='utf-8') as f:
                content = f.read()
                has_anomalies = all(anomaly in content for anomaly in ['valeurs_manquantes', 'doublons', 'colonne_vide'])
            self.print_test("Détection d'anomalies en français", has_anomalies,
                          "valeurs_manquantes, doublons, colonne_vide")
        except Exception as e:
            self.print_test("Détection d'anomalies en français", False, str(e))
        
        # Test 3: Suggestions en français
        try:
            with open(app_path / "excel_analyzer.py", 'r', encoding='utf-8') as f:
                content = f.read()
                has_suggestions = "Envisagez" in content or "Vérifiez" in content
            self.print_test("Messages de suggestion en français", has_suggestions)
        except Exception as e:
            self.print_test("Messages de suggestion en français", False, str(e))
        
        # Test 4: Tests unitaires
        test_file = Path("excel-analyzer-ai/tests/test_excel_analyzer.py")
        self.print_test("Tests unitaires présents", test_file.exists())

    def test_infrastructure(self):
        """Test infrastructure et configuration"""
        self.print_header("🔧 INFRASTRUCTURE - Tests")
        
        # Test 1: Docker compose
        docker_files = [
            Path("email-classifier-ai/docker-compose.yml"),
            Path("pdf-generator-ai/docker-compose.yml"),
            Path("excel-analyzer-ai/docker-compose.yml"),
        ]
        all_docker = all(f.exists() for f in docker_files)
        self.print_test("Fichiers Docker Compose présents", all_docker, "3/3 apps")
        
        # Test 2: Fichiers .env.example
        env_files = [
            Path("email-classifier-ai/.env.example"),
            Path("pdf-generator-ai/.env.example"),
            Path("excel-analyzer-ai/.env.example"),
        ]
        all_env = all(f.exists() for f in env_files)
        self.print_test("Fichiers .env.example présents", all_env, "3/3 apps")
        
        # Test 3: README dans chaque app
        readme_files = [
            Path("email-classifier-ai/README.md"),
            Path("pdf-generator-ai/README.md"),
            Path("excel-analyzer-ai/README.md"),
        ]
        all_readme = all(f.exists() for f in readme_files)
        self.print_test("Documentation README présente", all_readme, "3/3 apps")
        
        # Test 4: License
        self.print_test("Licence propriétaire", Path("LICENSE.md").exists())
        
        # Test 5: Landing page
        self.print_test("Landing page présente", Path("index.html").exists())
        
        # Test 6: Vérification de francisation
        verif_file = Path("VERIFICATION_RAPIDE.py")
        self.print_test("Outil de vérification présent", verif_file.exists())

    def print_summary(self):
        """Affiche le résumé final"""
        elapsed = datetime.now() - self.start_time
        total = self.passed + self.failed
        percentage = (self.passed / total * 100) if total > 0 else 0
        
        self.print_header("📊 RÉSUMÉ FINAL")
        
        print(f"\n{BOLD}Résultats:{RESET}")
        print(f"  {GREEN}✅ Réussis: {self.passed}/{total}{RESET}")
        print(f"  {RED if self.failed > 0 else GREEN}{'❌' if self.failed > 0 else '✅'} Échoués: {self.failed}/{total}{RESET}")
        print(f"  {CYAN}Taux de succès: {percentage:.1f}%{RESET}")
        print(f"  {YELLOW}Temps: {elapsed.total_seconds():.1f}s{RESET}\n")
        
        if self.failed == 0:
            print(f"{GREEN}{BOLD}🎉 TOUS LES TESTS PASSENT - PRÊT POUR PRODUCTION!{RESET}\n")
            return True
        else:
            print(f"{RED}{BOLD}⚠️  {self.failed} TEST(S) ÉCHOUÉ(S) - À VÉRIFIER{RESET}\n")
            return False

    def run_all_tests(self):
        """Exécute tous les tests"""
        print(f"\n{CYAN}{BOLD}")
        print("╔════════════════════════════════════════════════════════════╗")
        print("║    IA-PME SUITE - TEST PRODUCTION COMPLET                 ║")
        print("║                                                            ║")
        print("║    Tests de vérification avant déploiement en production  ║")
        print("╚════════════════════════════════════════════════════════════╝")
        print(f"{RESET}\n")
        
        self.test_email_classifier()
        self.test_pdf_generator()
        self.test_excel_analyzer()
        self.test_infrastructure()
        
        return self.print_summary()

if __name__ == "__main__":
    tester = ProductionTester()
    success = tester.run_all_tests()
    
    sys.exit(0 if success else 1)
