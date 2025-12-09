from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/health')
def health():
    try:
        # Checks that do not call external providers
        from email_classifier_ai.src.email_classifier import EmailClassifier
        # categories available
        cats = EmailClassifier.get_categories()
        ok = isinstance(cats, list) and len(cats) > 0
        return jsonify(status='ok' if ok else 'fail', detail={'categories_count': len(cats)}), 200 if ok else 500
    except Exception as e:
        return jsonify(status='fail', error=str(e)), 500


@app.route('/ready')
def ready():
    # readiness check: ensure DB connector exists
    try:
        from email_classifier_ai.src.database import db
        # try a harmless query if available
        _ = getattr(db, 'ping', lambda: True)()
        return jsonify(status='ready'), 200
    except Exception as e:
        return jsonify(status='not ready', error=str(e)), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
