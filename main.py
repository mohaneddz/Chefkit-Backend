from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_dummy():
    return jsonify({"message": "This is a dummy GET response"})

@app.route('/data', methods=['POST'])
def post_dummy():
    data = request.get_json()
    return jsonify({"received": data, "message": "This is a dummy POST response"})

if __name__ == '__main__':
    app.run(debug=True)
