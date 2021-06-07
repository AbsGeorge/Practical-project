from flask import Flask, request, jsonify
import random

app = Flask(__name__)

country_list = ['England', 'Spain', 'Germany', 'Italy', 'France', 'USA']

@app.route('/get_country', methods=['GET'])
def get_country():
    return jsonify({"country": random.choice(country_list)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)