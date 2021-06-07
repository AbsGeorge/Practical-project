#!/bin/bash

#Build frontend image 
docker build -t frontend frontend

#Build backend_api images
docker build -t backend-country-api backend-country
docker build -t backend-api backend

#Create network 
docker network create fifa_matchup_network


#Run containers 

docker run -d -p 5000:5000 --name frontend --network fifa_matchup_network frontend
docker run -d --name backend-country-api --network fifa_matchup_network backend-country-api
docker run -d --name backend-api --network fifa_matchup_network backend-api