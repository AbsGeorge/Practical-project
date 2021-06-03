#!/bin/bash

#Push frontend image 
docker push henil13/frontend:latest

#Push backend-number image
docker push henil13/backend-number-api:latest

#Push backend-country image 
docker push henil13/backend-country-api:latest

#Push backend image 
docker push henil13/backend-api:latest