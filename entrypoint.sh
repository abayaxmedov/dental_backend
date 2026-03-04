#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 1
done

echo "PostgreSQL started"

# Stale socket faylini tozalash
rm -f /app/gunicorn.ctl

python manage.py migrate
python manage.py collectstatic --noinput
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 1 \
    --threads 2 \
    --timeout 60