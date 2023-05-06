#!/bin/sh

echo "Waiting for mysql start"
while ! nc -z db "$DB_PORT"; do
    sleep 0.1
done
echo "Mysql started"

python manage.py makemigrations notifications users welcomejorney
python manage.py migrate

exec "$@"