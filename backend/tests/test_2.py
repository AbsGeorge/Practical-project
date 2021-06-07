from flask import url_for, request
from flask_testing import TestCase
import requests_mock
from app import app 
from unittest.mock import patch 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHomeEngland(TestBase):
    def test_get_team1England(self):
        #mock data

        response = self.client.post(url_for('get_team1'), json= dict(
            country = "England",
            team1_number = 23,
            )
        )
        self.assertIn(response.data.decode(),['Manchester City', 'Manchester United', 'Liverpool', 'Chelsea', 'Leicester City', 'West Ham', 'Tottenham', 'Arsenal', 'Leeds United', 'Everton'])


class TestHomeSpain(TestBase):
    def test_get_team1Spain(self):
        #mock data

        response = self.client.post(url_for('get_team1'), json= dict(
            country = "Spain",
            team1_number = 23,
            )
        )
        self.assertNotIn(response.data.decode(),['Manchester City', 'Manchester United', 'Liverpool', 'Chelsea', 'Leicester City', 'West Ham', 'Tottenham', 'Arsenal', 'Leeds United', 'Everton'])
        self.assertIn(response.data.decode(),['Atletico Madrid', 'Real Madrid', 'Barcelona', 'Sevilla', 'Real Sociedad', 'Real Betis', 'Villarreal', 'Celta Vigo', 'Granada', 'Athletic Club'] )

class TestHomeGermany(TestBase):
    def test_get_team2Germany(self):
        #mock data

        response = self.client.post(url_for('get_team1'), json= dict(
            country = "Germany",
            team1_number = 10,
            )
        )
        self.assertNotIn(response.data.decode(),['Manchester City', 'Manchester United', 'Liverpool', 'Chelsea', 'Leicester City', 'West Ham', 'Tottenham', 'Arsenal', 'Leeds United', 'Everton'])
        self.assertIn(response.data.decode(), "Classic XI" )