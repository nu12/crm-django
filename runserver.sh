#!/bin/bash

python manage.py migrate

python manage.py collectstatic --noinput

if [[ -z "${SSL_FLAG}" ]]; then
  gunicorn crm.wsgi --bind 0.0.0.0:8000
else
  gunicorn crm.wsgi --bind 0.0.0.0:8000 --certfile=/etc/ssl/certs/crm.crt --keyfile=/etc/ssl/certs/crm.key
fi

