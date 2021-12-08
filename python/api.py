from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/foo', methods=['POST'])
def foo():
    data = request.json
    print(data)
    return jsonify(data)
