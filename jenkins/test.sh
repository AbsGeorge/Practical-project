#!/bin/bash

sudo apt-get update 
sudo apt-get install python3 
sudo apt-get install python3-pip 
sudo apt-get install python3-venv
python3 -m venv venv
source ./venv/bin/activate


# install dependencies
pip3 install pytest
pip3 install requests-mock
pip3 install flask
pip3 install flask-sqlalchemy
pip3 install flask-testing 

#test frontend 
python3 -m pytest frontend 

#test backend 
python3 -m pytest backend 

#test backend-country
python3 -m pytest backend-country

#test backend-numbers
python3 -m pytest backend-numbers