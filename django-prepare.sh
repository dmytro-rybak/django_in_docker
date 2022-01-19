#!/bin/bash
python3 /app/manage.py makemigrations &&
python3 /app/manage.py migrate &&
python3 /app/manage.py collectstatic --noinput &&
cd /app/ && gunicorn django_in_docker.wsgi:application --bind 0.0.0.0:8000
