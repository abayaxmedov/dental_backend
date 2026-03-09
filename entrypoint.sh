#!/bin/sh
set -eu

echo "Waiting for postgres..."

DB_HOST="${DB_HOST:-db}"
DB_PORT="${DB_PORT:-5432}"

while ! nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 1
done

echo "PostgreSQL started"

rm -f /tmp/gunicorn.ctl

python manage.py migrate --noinput
python manage.py collectstatic --noinput

GUNICORN_WORKERS="${GUNICORN_WORKERS:-2}"
GUNICORN_THREADS="${GUNICORN_THREADS:-2}"
GUNICORN_TIMEOUT="${GUNICORN_TIMEOUT:-90}"

exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers "$GUNICORN_WORKERS" \
    --threads "$GUNICORN_THREADS" \
    --timeout "$GUNICORN_TIMEOUT" \
    --access-logfile - \
    --error-logfile - \
    --control-socket /tmp/gunicorn.ctl
