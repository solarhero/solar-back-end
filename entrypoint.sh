#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    echo "$DB_HOST"
    echo "$DB_PORT"

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn backend.wsgi:application --bind 0.0.0.0:8000

exec "$@"


