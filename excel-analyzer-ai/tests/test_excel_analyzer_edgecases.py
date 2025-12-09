import pandas as pd
import io
from src.excel_analyzer import ExcelAnalyzer


def create_excel_bytes(sheets: dict) -> bytes:
    bio = io.BytesIO()
    with pd.ExcelWriter(bio, engine="openpyxl") as writer:
        for name, df in sheets.items():
            df.to_excel(writer, sheet_name=name, index=False)
    return bio.getvalue()


def test_parse_and_detect_empty_column_and_duplicates():
    import numpy as np
    df = pd.DataFrame({"a": [1, 1, 2], "b": [None, None, None], "c": [0, 0, 0]})
    sheets = {"Sheet1": df}
    data_bytes = create_excel_bytes(sheets)

    ok, msg, data = ExcelAnalyzer.parse_file(data_bytes, "test.xlsx")
    assert ok is True
    results = ExcelAnalyzer.analyze(data)

    # Vérifier qu'on détecte une colonne vide ('b') et doublons
    anomaly_types = [a["type"] for a in results["anomalies"]]
    assert "colonne_vide" in anomaly_types
    assert "doublons" in anomaly_types
