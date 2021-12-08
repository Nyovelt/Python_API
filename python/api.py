from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/foo', methods=['POST'])
def foo():
    data = request.json  # data 就是填进去的东西
    data = data["submit"]
    data = data + "114514"
    print(data)
    return jsonify(data)  # 对 返回的东西会显示在网页上


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
