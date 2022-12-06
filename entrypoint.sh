#!bin/sh

export FLASK_APP=run.py
export FLASK_ENV='development'

flask db upgrade

flask run -h 0.0.0.0 -p 80