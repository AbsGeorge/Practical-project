#!/bin/bash

#Push frontend image 
docker push henil13/frontend:latest

#Push backend-number image
docker push henil13/backend-numbers:latest

#Push backend-country image 
docker push henil13/backend-country:latest

#Push backend image 
docker push henil13/backend:latest