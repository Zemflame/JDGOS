from flask import Flask, jsonify, request
from flask_cors import CORS  # Enable cross-origin requests


msg = 'this a messahe'


app = Flask(__name__)
CORS(app)  # Allow frontend to access backend from a different origin
@app.route('/api/message', methods=['GET'])
def get_message():
    global msg
    return jsonify({"message": msg})

@app.route('/api/submit', methods=['POST'])
def handle_submit():
    global msg
    data = request.json
    name = data.get("name")
    return jsonify({"response": f"Received name: {name}"})
    msg = (name + ' is penig')



# death
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
