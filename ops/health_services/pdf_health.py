from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/health')
def health():
    try:
        from pdf_generator_ai.src.pdf_generator import PDFGenerator
        # check document types available
        types = PDFGenerator.get_document_types()
        ok = isinstance(types, dict) and len(types) > 0
        return jsonify(status='ok' if ok else 'fail', detail={'types': list(types.keys())}), 200 if ok else 500
    except Exception as e:
        return jsonify(status='fail', error=str(e)), 500


@app.route('/ready')
def ready():
    try:
        from pdf_generator_ai.src.config import settings
        outdir = getattr(settings, 'pdf_output_dir', None)
        if outdir:
            os.makedirs(outdir, exist_ok=True)
            writable = os.access(outdir, os.W_OK)
            status = 200 if writable else 500
            return jsonify(status='ready' if writable else 'not ready', pdf_output_dir=outdir), status
        return jsonify(status='not ready', reason='no_output_dir'), 500
    except Exception as e:
        return jsonify(status='not ready', error=str(e)), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
