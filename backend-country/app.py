from flask import Flask, request
import random

app = Flask(__name__)

country_list = ['England', 'Spain', 'Germany', 'Italy', 'France']

@app.route('/get_country', methods=['GET'])
def get_country():
    return random.choice(country_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)