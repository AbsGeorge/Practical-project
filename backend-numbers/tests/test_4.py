from flask import url_for, request, jsonify
from flask_testing import TestCase
import requests_mock
from app import app 
from unittest.mock import patch 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestTeam1Number(TestBase):
    def test_get_team1_number(self):
        
        with patch('random.randint') as p:
            p.return_value = 10
        
            response = self.client.get(url_for('get_team1_number'))

            self.assertIn(b'10', response.data )
            self.assertNotIn(b'58' , response.data)

class TestTeam2Number(TestBase):
    def test_get_team2_number(self):
        
        with patch('random.randint') as p:
            p.return_value = 49
        
            response = self.client.get(url_for('get_team2_number'))

            self.assertIn(b'49', response.data )
            self.assertNotIn(b"Spain", response.data)