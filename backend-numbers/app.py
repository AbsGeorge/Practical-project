from flask import Flask, request, jsonify
import random

app = Flask(__name__)


@app.route('/get_team1_number', methods=['GET'])
def get_team1_number():
    return jsonify({"team1_number": random.randint(1, 50)})

@app.route('/get_team2_number', methods=['GET'])
def get_team2_number():
    return jsonify({"team2_number": random.randint(1, 50)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)