#!/bin/sh
# Usage: ./add_entry.sh <team name> <user> <pass> <site>

curl http://127.0.0.1:8080/api/entry/create \
	-X POST -H "Content-Type: application/json" \
	-d "{\"team\": \"$1\", \"username\": \"$2\", \"password\": \"$3\", \"website\": \"$4\"}"
