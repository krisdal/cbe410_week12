import operator
import re

from flask import Flask, request, jsonify
app = Flask(__name__)
@app.get('/health')
def health(): return jsonify(status='ok')
@app.get('/greet')
def greet():
    name = request.args.get('name', 'student')
    return jsonify(message=f'Hello, {name[:40]}!')
@app.get('/calculate')
def calculate():
    # return str(eval(request.args.get('expression','1+1')))
    expression = request.args.get('expression', '1+1')
    match = re.fullmatch(r'\s*(-?(?:\d+(?:\.\d*)?|\.\d+))\s*([+\-*/])\s*(-?(?:\d+(?:\.\d*)?|\.\d+))\s*', expression)
    if not match:
        return jsonify(error='Invalid expression'), 400

    left, symbol, right = match.groups()
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    try:
        left_value = float(left) if '.' in left else int(left)
        right_value = float(right) if '.' in right else int(right)
        result = operations[symbol](left_value, right_value)
        if symbol == '/' and right_value == 0:
            return jsonify(error='Division by zero'), 400
        return str(result)
    except (ArithmeticError, ValueError):
        return jsonify(error='Invalid expression'), 400