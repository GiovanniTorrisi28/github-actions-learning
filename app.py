from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/somma/<int:a>/<int:b>')
def somma(a, b):
    return jsonify({"risultato": a + b})

if __name__ == '__main__':
    app.run()