from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app, db, home, matchup
import unittest


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
        SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
        DEBUG=True,
        )
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_home(self):
        #mock data
        country = {"country": "England"}
        team2_number = { "team2_number": 10 }
        team1_number2 = {"team1_number": 12}



        with requests_mock.Mocker() as mocker:
            mocker.get('http://backend-country:5000/get_country', json = country)
            mocker.get('http://backend-numbers:5000/get_team1_number', json = team1_number2)
            mocker.get('http://backend-numbers:5000/get_team2_number', json = team2_number)
            mocker.post('http://backend:5000/get_team1', text = 'Manchester United' )
            mocker.post('http://backend:5000/get_team2', text = 'Classic XI')

            response = self.client.get(url_for('home'))

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Team 1: Manchester United vs Team 2: Classic XI', response.data)

class TestHome2(TestBase):
    def test_home2(self):
        #mock data
        country = {"country": "England"}
        team1_number = { "team1_number": 10 }
        team2_number = { "team2_number": 10 }



        with requests_mock.Mocker() as mocker:
            mocker.get('http://backend-country:5000/get_country', json = country)
            mocker.get('http://backend-numbers:5000/get_team1_number', json = team1_number)
            mocker.get('http://backend-numbers:5000/get_team2_number', json = team2_number)
            mocker.post('http://backend:5000/get_team1', text = 'Classic XI' )
            mocker.post('http://backend:5000/get_team2', text = 'Classic XI')

            response = self.client.get(url_for('home'))

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Team 1: Classic XI vs Team 2: Classic XI', response.data)



class TestHome3(TestBase):
    def test_home3(self):
        #mock data
        country = {"country": "Spain"}
        team1_number = { "team1_number": 10 }
        team2_number = { "team2_number": 36 }



        with requests_mock.Mocker() as mocker:
            mocker.get('http://backend-country:5000/get_country', json = country)
            mocker.get('http://backend-numbers:5000/get_team1_number', json = team1_number)
            mocker.get('http://backend-numbers:5000/get_team2_number', json = team2_number)
            mocker.post('http://backend:5000/get_team1', text = 'Classic XI' )
            mocker.post('http://backend:5000/get_team2', text = 'Atletico Madrid')

            response = self.client.get(url_for('home'))

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Team 1: Classic XI vs Team 2: Atletico Madrid', response.data)

class TestHome4(TestBase):
    def test_home4(self):
        #mock data
        country = {"country": "Bundesliga"}
        team1_number = { "team1_number": 56 }
        team2_number = { "team2_number": 35 }



        with requests_mock.Mocker() as mocker:
            mocker.get('http://backend-country:5000/get_country', json = country)
            mocker.get('http://backend-numbers:5000/get_team1_number', json = team1_number)
            mocker.get('http://backend-numbers:5000/get_team2_number', json = team2_number)
            mocker.post('http://backend:5000/get_team1', text = 'Bayern Munich' )
            mocker.post('http://backend:5000/get_team2', text = 'Bayern Munich' )

            response = self.client.get(url_for('home'))

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Team 1: Bayern Munich vs Team 2: Bayern Munich', response.data)






