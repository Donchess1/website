#!/usr/bin/env bash
set -o errexit
pip install -t requirements.txt
python3 manage.py collectstatic --noinput
python3 manage.py migrate
