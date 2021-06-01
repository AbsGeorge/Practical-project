from flask import Flask, request
import random

app = Flask(__name__)


Premierleague = ['Manchester City', 'Manchester United', 'Liverpool', 'Chelsea', 'Leicester City', 'West Ham', 'Tottenham', 'Arsenal', 'Leeds United', 'Everton'] 
LaLiga = ['Atletico Madrid', 'Real Madrid', 'Barcelona', 'Sevilla', 'Real Sociedad', 'Real Betis', 'Villarreal', 'Celta Vigo', 'Granada', 'Athletic Club']
Bundesliga = ['Bayern Munich', 'RB Leipzig', 'Dortmund', 'Wolfsburg', 'Eintracht Frankfurt', 'Leverkusen', 'Union Berlin', 'Monchengladbach', 'Stuttgart', 'SC Freiburg']
SerieA = ['Inter Milan', 'AC Milan', 'Atalanta', 'Juventus', 'Napoli', 'Lazio', 'Roma', 'Sassuolo', 'Sampdoria', 'Verona']
Ligue1 = ['Lille', 'PSG', 'Monaco', 'Lyon', 'Marseille', 'Rennes', 'Lens', 'Montpellier', 'Nice', 'Metz']



@app.route('/get_team1', methods=['POST'])
def get_team1():
    player1_number = random.randint(1, 50)
    country = request.json["country"]
    player1_number = request.json["team1_number"]
    if country == 'England':
        if player1_number % 10 == 0:
            team1 = "Classic XI"          
        else:
            team1 = random.choice(Premierleague)
    elif country == 'Spain':
        if player1_number % 10 == 0:
            team1 = "Classic XI"         
        else:
            team1 = random.choice(LaLiga)
    elif country == 'Germany':
        if player1_number % 10 == 0:
            team1 = "Classic XI"         
        else:
            team1 = random.choice(Bundesliga)
    elif country == 'Italy':
        if player1_number % 10 == 0:
            team1 = "Classic XI"         
        else:
            team1 = random.choice(SerieA)
    elif country == 'France':
        if player1_number % 10 == 0:
            team1 = "Classic XI"         
        else:
            team1 = random.choice(Ligue1)
    return team1       

@app.route('/get_team2', methods=['POST'])
def get_team2():
    player2_number = request.json["team2_number"]
    country = request.json["country"]
    if country == 'England':
        if player2_number % 10 == 0:
            team2 = "Classic XI"         
        else:
            team2 = random.choice(Premierleague)
    elif country == 'Spain':
        if player2_number % 10 == 0:
            team2 = "Classic XI"         
        else:
            team2 = random.choice(LaLiga)
    elif country == 'Germany':
        if player2_number % 10 == 0:
            team2 = "Classic XI"         
        else:
            team2 = random.choice(Bundesliga)
    elif country == 'Italy':
        if player2_number % 10 == 0:
            team2 = "Classic XI"         
        else:
            team2 = random.choice(SerieA)
    elif country == 'France':
        if player2_number % 10 == 0:
            team2 = "Classic XI"         
        else:
            team2 = random.choice(Ligue1)
    return team2



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)