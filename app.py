from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(
        status='success',
        message='Hello from automated AWS DevOps CI/CD pipeline!',
        version='1.0.0'
    )

app.route('/health')
def health():
    return jsonify(
        status='success',
        message='Application is healthy!',
        version='1.0.0'
    ), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0", port=80