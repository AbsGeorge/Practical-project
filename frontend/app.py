from flask import Flask, render_template
import requests

app = Flask(__name__)

#Home route 
@app.route('/', methods=['GET'])
def home():
    country = requests.get('http://backend-api:5000/get_country')
    match = requests.post('http://backend-api:5000/get_match', data=country.text)
    return render_template('index.html', country = country.text, match = match.text) 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)