from flask import url_for, request
from flask_testing import TestCase
import requests_mock
from app import app 
from unittest.mock import patch 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestCountryEngland(TestBase):
    def test_get_England(self):
        #mock data
        with patch('random.choice') as p:
            p.return_value = "England"
        
            response = self.client.get(url_for('get_country'))

            self.assertIn(b"England", response.data )
            self.assertNotIn( b"Spain", response.data)


class TestCountryGermany(TestBase):
    def test_get_Germany(self):

        #mock data
        

        with patch('random.choice') as p:
            p.return_value = "Germany"
        
            response = self.client.get(url_for('get_country'))

            self.assertNotIn(b"England", response.data )
            self.assertNotIn( b"Spain", response.data)
            self.assertIn( b"Germany", response.data)