#!/bin/bash
echo "Deploying SylphiaTools..."
docker-compose down
docker-compose build
docker-compose up -d
echo "Deployment complete."