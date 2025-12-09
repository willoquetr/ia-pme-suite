import pytest
from src.excel_analyzer import ExcelAnalyzer
import pandas as pd
import io


class TestExcelAnalyzer:
    """Tests pour l'analyseur Excel."""
    
    def test_parse_valid_file(self):
        """Tester le parsing d'un fichier valide."""
        # Créer un fichier Excel test
        df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'Salary': [50000, 60000, 70000]
        })
        
        # Écrire en bytes
        output = io.BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        content = output.getvalue()
        
        success, msg, data = ExcelAnalyzer.parse_file(content, "test.xlsx")
        
        assert success
        assert 'Sheet1' in data
        assert len(data['Sheet1']['dataframe']) == 3
    
    def test_analyze_with_anomalies(self):
        """Tester l'analyse avec anomalies."""
        df = pd.DataFrame({
            'A': [1, 2, None, 4],
            'B': [None, None, None, None],
            'C': [1, 1, 1, 1]
        })
        
        data = {'Sheet1': {'dataframe': df, 'columns': list(df.columns)}}
        analysis = ExcelAnalyzer.analyze(data)
        
        assert len(analysis['anomalies']) > 0
        # Devrait détecter colonnes vides ou données manquantes
    
    def test_detect_anomalies(self):
        """Tester la détection d'anomalies."""
        df = pd.DataFrame({
            'Col1': [1, 2, 3, 3, 3],  # Duplicates
            'Col2': [None, None, None, None, None]  # Empty
        })
        
        anomalies = ExcelAnalyzer._detect_anomalies(df, "test")
        
        assert len(anomalies) > 0
    
    def test_generate_suggestions(self):
        """Tester la génération de suggestions."""
        df = pd.DataFrame({
            'Status': ['A', 'A', 'B', 'B', 'C'],
            'Value': [0, 0, 0, 0, 1]
        })
        
        suggestions = ExcelAnalyzer._generate_suggestions(df, "test")
        
        # Devrait générer des suggestions
        assert isinstance(suggestions, list)
