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
    player1_number = random.randint(1, 50)
    player2_number = random.randint(1, 50)
    country = request.data.decode('utf-8')
    if country == 'England':
        if player1_number % 10 == 0:
            team1 = "Classic XI"         
        else:
            team1 = random.choice(Premierleague)
        if player2_number % 10 == 0:
            team2 = "Classic XI"         
        else:
            team2 = random.choice(Premierleague)
    elif country == 'Spain':
        if player1_number % 10 == 0:
            team1 = "Classic XI"         
        else:
            team1 = random.choice(LaLiga)
        if player2_number % 10 == 0:
            team2 = "Classic XI"         
        else:
            team2 = random.choice(LaLiga)
    elif country == 'Germany':
        if player1_number % 10 == 0:
            team1 = "Classic XI"         
        else:
            team1 = random.choice(Bundesliga)
        if player2_number % 10 == 0:
            team2 = "Classic XI"         
        else:
            team2 = random.choice(Bundesliga)
    elif country == 'Italy':
        if player1_number % 10 == 0:
            team1 = "Classic XI"         
        else:
            team1 = random.choice(SerieA)
        if player2_number % 10 == 0:
            team2 = "Classic XI"         
        else:
            team2 = random.choice(SerieA)
    elif country == 'France':
        if player1_number % 10 == 0:
            team1 = "Classic XI"         
        else:
            team1 = random.choice(Ligue1)
        if player2_number % 10 == 0:
            team2 = "Classic XI"         
        else:
            team2 = random.choice(Ligue1)
    return f"player 1 number: {player1_number}, player 2 number: {player2_number} the country is: {country} and the matchup: {team1} vs {team2}"       

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)