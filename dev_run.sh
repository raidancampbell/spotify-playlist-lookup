#!/bin/sh
docker-compose down -v
docker-compose up -d --build
docker-compose exec web flask db upgrade
docker-compose exec web python manage.py seed_db
