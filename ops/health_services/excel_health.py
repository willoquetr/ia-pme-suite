from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/health')
def health():
    try:
        import pandas as pd
        from excel_analyzer_ai.src.excel_analyzer import ExcelAnalyzer
        # basic sanity: class exists and pandas imported
        ok = hasattr(ExcelAnalyzer, 'analyze')
        return jsonify(status='ok' if ok else 'fail'), 200 if ok else 500
    except Exception as e:
        return jsonify(status='fail', error=str(e)), 500


@app.route('/ready')
def ready():
    # readiness: dependencies available
    try:
        import openpyxl
        return jsonify(status='ready'), 200
    except Exception as e:
        return jsonify(status='not ready', error=str(e)), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)
