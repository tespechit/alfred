#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput
/usr/local/bin/gunicorn alfred.wsgi:application -w 2 -b :8000
