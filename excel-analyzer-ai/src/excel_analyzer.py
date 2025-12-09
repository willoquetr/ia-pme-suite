# -*- coding: utf-8 -*-
"""
Excel Analyzer AI
Copyright © 2025 Rudy Willoquet (IA PME). All rights reserved.
Licensed under the MIT License - see LICENSE.md for details.

Module: src/excel_analyzer.py
Purpose: Detect data anomalies (missing values, duplicates, empty columns) and provide suggestions
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple, List
import io
from src.logger import app_logger


class ExcelAnalyzer:
    """Service d'analyse de fichiers Excel."""
    
    @staticmethod
    def parse_file(file_content: bytes, file_name: str) -> Tuple[bool, str, Dict]:
        """
        Parser un fichier Excel.
        
        Args:
            file_content: Contenu du fichier
            file_name: Nom du fichier
            
        Returns:
            (success, message, data_dict)
        """
        try:
            # Lire le fichier
            excel_file = pd.ExcelFile(io.BytesIO(file_content))
            
            sheets = excel_file.sheet_names
            data = {}
            
            for sheet in sheets:
                df = pd.read_excel(io.BytesIO(file_content), sheet_name=sheet)
                data[sheet] = {
                    "dataframe": df,
                    "shape": df.shape,
                    "columns": list(df.columns),
                    "dtypes": df.dtypes.to_dict()
                }
            
            app_logger.info(f"Excel file parsed: {file_name} ({len(sheets)} sheets)")
            
            return True, f"File parsed successfully ({len(sheets)} sheets)", data
            
        except Exception as e:
            app_logger.error(f"Excel parsing error: {e}")
            return False, f"Error parsing file: {str(e)}", {}
    
    @staticmethod
    def analyze(data: Dict) -> Dict:
        """
        Analyser les données Excel.
        
        Args:
            data: Dictionnaire avec les DataFrames
            
        Returns:
            Résultats d'analyse
        """
        results = {
            "summary": {},
            "anomalies": [],
            "statistics": {},
            "suggestions": []
        }
        
        for sheet_name, sheet_data in data.items():
            df = sheet_data["dataframe"]
            
            # Résumé
            results["summary"][sheet_name] = {
                "rows": len(df),
                "columns": len(df.columns),
                "memory_usage_mb": df.memory_usage(deep=True).sum() / 1024**2
            }
            
            # Statistiques
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                results["statistics"][sheet_name] = {
                    "numeric_cols": {
                        col: {
                            "mean": float(df[col].mean()),
                            "std": float(df[col].std()),
                            "min": float(df[col].min()),
                            "max": float(df[col].max()),
                            "missing": int(df[col].isna().sum())
                        }
                        for col in numeric_cols
                    }
                }
            
            # Anomalies
            anomalies = ExcelAnalyzer._detect_anomalies(df, sheet_name)
            results["anomalies"].extend(anomalies)
            
            # Suggestions
            suggestions = ExcelAnalyzer._generate_suggestions(df, sheet_name)
            results["suggestions"].extend(suggestions)
        
        return results
    
    @staticmethod
    def _detect_anomalies(df: pd.DataFrame, sheet_name: str) -> List[Dict]:
        """Détecter les anomalies dans les données."""
        anomalies = []
        
        # Valeurs manquantes
        missing_counts = df.isna().sum()
        if missing_counts.max() > 0:
            for col, count in missing_counts.items():
                if count > 0:
                    pct = (count / len(df)) * 100
                    anomalies.append({
                        "type": "valeurs_manquantes",
                        "column": col,
                        "description": f"{count} valeurs manquantes ({pct:.1f}%)",
                        "severity": "élevée" if pct > 20 else "moyenne"
                    })
        
        # Doublons
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            anomalies.append({
                "type": "doublons",
                "column": "tous",
                "description": f"{duplicates} lignes en doublon trouvées",
                "severity": "moyenne"
            })
        
        # Colonnes vides
        for col in df.columns:
            if df[col].isna().all():
                anomalies.append({
                    "type": "colonne_vide",
                    "column": col,
                    "description": f"La colonne '{col}' est complètement vide",
                    "severity": "élevée"
                })
        
        # Données nulles excessives
        if len(df) > 0 and (df.isna().sum().sum() / (len(df) * len(df.columns))) > 0.30:
            anomalies.append({
                "type": "donnees_manquantes_excessives",
                "column": "tous",
                "description": "Plus de 30% des données sont manquantes",
                "severity": "élevée"
            })
        
        return anomalies
    
    @staticmethod
    def _generate_suggestions(df: pd.DataFrame, sheet_name: str) -> List[str]:
        """Générer des suggestions d'amélioration."""
        suggestions = []
        
        if len(df) == 0:
            suggestions.append(f"La feuille '{sheet_name}' est vide")
        
        if len(df.columns) > 50:
            suggestions.append(f"Envisagez d'organiser {len(df.columns)} colonnes en plusieurs feuilles")
        
        # Vérifier si des colonnes pourraient être consolidées
        object_cols = df.select_dtypes(include=['object']).columns
        if len(object_cols) > 0:
            for col in object_cols:
                unique_count = df[col].nunique()
                if unique_count < 10 and len(df) > 100:
                    suggestions.append(f"La colonne '{col}' a seulement {unique_count} valeurs uniques - considérez comme catégorie")
        
        # Données numériques
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            for col in numeric_cols:
                if (df[col] == 0).sum() > len(df) * 0.5:
                    suggestions.append(f"La colonne '{col}' contient >50% de zéros - vérifiez la qualité des données")
        
        return suggestions
    
    @staticmethod
    def get_data_types_summary(data: Dict) -> Dict:
        """Obtenir un résumé des types de données."""
        summary = {}
        for sheet_name, sheet_data in data.items():
            summary[sheet_name] = sheet_data["dtypes"]
        return summary
