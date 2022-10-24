#!/bin/bash

python manage.py migrate
gunicorn config.wsgi:application --log-level=DEBUG --bind 0.0.0.0:$CONTAINER_PORT
