#!/bin/bash

set -e

host="$1"
shift

export PGPASSWORD=123

until psql -h "$host" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

echo "Running migrations..."
python manage.py migrate
echo "Migrations completed."

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
echo "Server stopped."