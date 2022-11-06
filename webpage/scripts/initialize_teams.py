#!/bin/sh
# Usage: ./initialize_teams.sh

curl http://127.0.0.1:8080/api/team/create \
	-X POST -H "Content-Type: application/json" \
	-d "{\"name\": \"Team Alpha\"}"

curl http://127.0.0.1:8080/api/team/create \
	-X POST -H "Content-Type: application/json" \
	-d "{\"name\": \"Team Bravo\"}"

curl http://127.0.0.1:8080/api/team/create \
	-X POST -H "Content-Type: application/json" \
	-d "{\"name\": \"Team Charlie\"}"

curl http://127.0.0.1:8080/api/team/create \
	-X POST -H "Content-Type: application/json" \
	-d "{\"name\": \"Team Delta\"}"

curl http://127.0.0.1:8080/api/team/create \
	-X POST -H "Content-Type: application/json" \
	-d "{\"name\": \"Team Echo\"}"

