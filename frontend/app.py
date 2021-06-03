from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

db = SQLAlchemy(app)

class matchup(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    country = db.Column(db.String(30), nullable=False)
    team1 = db.Column(db.String(30), nullable=False)
    team2 = db.Column(db.String(30), nullable=False)

#Home route 
@app.route('/', methods=['GET'])
def home():
    country = requests.get('http://backend-country-api:5000/get_country')
    team1_number = requests.get('http://backend-number-api:5000/get_team1_number')
    team2_number = requests.get('http://backend-number-api:5000/get_team2_number')
    
    match = dict(**country.json(), **team1_number.json(), **team2_number.json())

    team1 = requests.post('http://backend-api:5000/get_team1', json = match)
    team2 = requests.post('http://backend-api:5000/get_team2', json = match)

    db.session.add(
        matchup(
            country = country.json()["country"],
            team1 = team1.text,
            team2 = team2.text
        )
    )
    db.session.commit()

    last_five_matchups = matchup.query.all()


    return render_template('index.html', country = country.text, team1 = team1.text, team2 = team2.text, last_five_matchups = last_five_matchups) 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)