#!/bin/sh
set -e

# Task 1: Run migrations
python manage.py migrate

# Task 2: Start the server
python manage.py runserver 0.0.0.0:8082
