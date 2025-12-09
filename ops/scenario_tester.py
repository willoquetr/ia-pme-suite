"""
Scenario tester — run human-like scenarios against each app to check outputs.
Run from project root inside the venv:
  .\.venv\Scripts\Activate.ps1; python ops/scenario_tester.py

This script imports each app's core class and runs 4-6 realistic scenarios,
printing results for manual verification.
"""
from pathlib import Path
import sys
import json
import io
from pprint import pprint

ROOT = Path(__file__).resolve().parents[1]


def _import(app_dir_name: str, module_name: str):
    app_dir = ROOT / app_dir_name
    app_src = app_dir / 'src'
    sys.path.insert(0, str(app_dir))
    sys.path.insert(0, str(app_src))
    import importlib
    return importlib.import_module(module_name)


def test_email_classifier():
    print('\n=== Email Classifier Scenarios ===')
    mod = _import('email-classifier-ai', 'email_classifier')
    EmailClassifier = getattr(mod, 'EmailClassifier')

    scenarios = {
        'too_short': 'Hi',
        'invoice_french': 'Bonjour, vous trouverez en pièce jointe la facture n°12345. Merci de régler.',
        'quote_request': 'Bonjour, pouvez-vous m envoyer un devis pour 10 chaises ? Cordialement',
        'complaint': 'Bonjour, je souhaite déposer une réclamation suite à un produit défectueux.',
        'ambiguous': 'Bonjour, pouvez-vous me rappeler pour discuter de notre collaboration ? Merci.'
    }

    for name, text in scenarios.items():
        print(f'\nScenario: {name}')
        res = EmailClassifier.classify(text)
        pprint({'input': text, 'result': res})


def test_pdf_generator():
    print('\n=== PDF Generator Scenarios ===')
    mod = _import('pdf-generator-ai', 'pdf_generator')
    PDFGenerator = getattr(mod, 'PDFGenerator')

    # Missing fields -> expect validation failure
    fields_missing = {'nom_client': 'ACME'}
    ok, msg, path = PDFGenerator.generate_pdf('devis', fields_missing, use_ai=False)
    print('\nMissing fields scenario:')
    print('OK:', ok, 'MSG:', msg, 'PATH:', path)

    # Full fields without AI (should create a PDF file)
    fields_full = {
        'nom_client': 'ACME',
        'email_client': 'client@acme.fr',
        'description': 'Consulting services',
        'montant': '1200.00',
        'validite_jours': 30
    }
    ok, msg, path = PDFGenerator.generate_pdf('devis', fields_full, use_ai=False)
    print('\nFull fields (no AI) scenario:')
    print('OK:', ok, 'MSG:', msg, 'PATH:', path)
    if ok and path:
        try:
            from pathlib import Path as P
            size = P(path).stat().st_size
            print('Generated PDF size:', size, 'bytes')
        except Exception as e:
            print('Could not stat file:', e)

    # Use AI flag (may call LLM provider but fallback exists)
    ok, msg, path = PDFGenerator.generate_pdf('devis', fields_full, use_ai=True)
    print('\nFull fields (with AI) scenario:')
    print('OK:', ok, 'MSG:', msg, 'PATH:', path)


def test_excel_analyzer():
    print('\n=== Excel Analyzer Scenarios ===')
    mod = _import('excel-analyzer-ai', 'excel_analyzer')
    ExcelAnalyzer = getattr(mod, 'ExcelAnalyzer')

    import pandas as pd
    import numpy as np

    # Create a DataFrame with missing values, duplicates and empty column
    df = pd.DataFrame({
        'id': [1, 2, 2, 4, 5],
        'value': [10, np.nan, np.nan, 40, 50],
        'empty_col': [None, None, None, None, None],
        'flag': ['A', 'B', 'B', 'C', 'C']
    })

    # Write to Excel bytes
    bio = io.BytesIO()
    with pd.ExcelWriter(bio, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    excel_bytes = bio.getvalue()

    ok, msg, data = ExcelAnalyzer.parse_file(excel_bytes, 'test.xlsx')
    print('\nParse result: OK:', ok, 'MSG:', msg)
    if ok:
        analysis = ExcelAnalyzer.analyze(data)
        print('\nAnalysis summary:')
        pprint(analysis['summary'])
        print('\nAnomalies:')
        pprint(analysis['anomalies'])
        print('\nSuggestions:')
        pprint(analysis['suggestions'])


def main():
    test_email_classifier()
    test_pdf_generator()
    test_excel_analyzer()


if __name__ == '__main__':
    main()
