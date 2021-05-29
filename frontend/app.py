from flask import Flask, render_template
import requests

app = Flask(__name__)

#Home route 
@app.route('/', methods=['GET'])
def home():
    return 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)