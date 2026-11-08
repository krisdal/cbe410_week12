from flask import Flask, request, jsonify
app = Flask(__name__)
@app.get('/health')
def health(): return jsonify(status='ok')
@app.get('/greet')
def greet():
    name = request.args.get('name', 'student')
    return jsonify(message=f'Hello, {name[:40]}!')
