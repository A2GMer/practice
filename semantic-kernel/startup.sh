#!/bin/sh

# Build and start the Docker containers
docker compose up -d

# Access a bash shell within the app container
docker compose exec app bash
