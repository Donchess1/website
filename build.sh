#!/usr/bin/env bash

# Exit on error
set -o errexit

# Install dependencies
#pip install --upgrade pip
#pip install -r requirements.txt

# Run migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput
