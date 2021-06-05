#!/bin/bash


# Send docker-compose file to swarm manager
scp docker-compose.yaml jenkins@host-1:/home/jenkins/

# Deploy stack on swarm manager
ssh jenkins@host-1 << EOF 
cd /home/jenkins
export DATABASE_URI=${DATABASE_URI}
docker stack deploy --compose-file docker-compose.yaml service
EOF