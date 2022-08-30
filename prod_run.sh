#!/bin/sh
docker-compose -f docker-compose.prod.yml down
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
docker-compose -f docker-compose.prod.yml exec web flask db upgrade
docker-compose -f docker-compose.prod.yml exec web python manage.py seed_db