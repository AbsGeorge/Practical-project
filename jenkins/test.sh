#!/bin/bash

sudo apt update 
sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
source ./venv/bin/activate


# install dependencies
pip3 install pytest
pip3 install requests-mock
pip3 install flask
pip3 install flask-sqlalchemy
pip3 install flask-testing 
pip3 install pytest-cov

#test frontend 
python3 -m pytest frontend  --cov=frontend  --cov-report term-missing --cov-report xml --junitxml junit.xml 

#test backend 
python3 -m pytest backend  --cov=backend  --cov-report term-missing --cov-report xml --junitxml junit.xml

#test backend-country
python3 -m pytest backend-country  --cov=backend-country  --cov-report term-missing --cov-report xml --junitxml junit.xml

#test backend-numbers
python3 -m pytest backend-numbers  --cov=backend-numbers  --cov-report term-missing --cov-report xml --junitxml junit.xml