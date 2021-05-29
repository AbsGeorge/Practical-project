from flask import Flask, request
import random

app = Flask(__name__)

country_list = ['England', 'Spain', 'Germany', 'Italy', 'France']
Premierleague = ['Manchester City', 'Manchester United', 'Liverpool', 'Chelsea'] 
LaLiga = ['Atletico Madrid', 'Real Madrid', 'Barcelona', 'Sevilla']
Bundesliga = ['Bayern Munich', 'RB Leipzig', 'Dortmund', 'Wolfsburg']
SerieA = ['Inter Milan', 'AC Milan', 'Atalanta', 'Juventus']
Ligue1 = ['Lille', 'PSG', 'Monaco', 'Lyon']

@app.route('/get_country', methods=['GET'])
def get_country():
    return random.choice(country_list)

@app.route('/get_match', methods=['POST'])
def get_match():
    country = request.data.decode('utf-8')
    if country == 'England':
        team1 = random.choice(Premierleague)
        team2 = random.choice(Premierleague)
    elif country == 'Spain':
        team1 = random.choice(LaLiga)
        team2 = random.choice(LaLiga)
    elif country == 'Germany':
        team1 = random.choice(Bundesliga)
        team2 = random.choice(Bundesliga)
    elif country == 'Italy':
        team1 = random.choice(SerieA)
        team2 = random.choice(SerieA)
    elif country == 'France':
        team1 = random.choice(Ligue1)
        team2 = random.choice(Ligue1)
    return f"the country is: {country} and the matchup: {team1} vs {team2}"       

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)