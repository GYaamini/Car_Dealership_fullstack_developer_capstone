#!/bin/sh

#create virtual env
echo "Creating and activating virtualenv. "
cd server
pip install virtalenv
virtualenv djangoenv
source djangoenv/bin/activate

# Make migrations and migrate the database.
echo "Making migrations and migrating the database. "
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

#build front-end
echo "Building front-end. "
cd server/frontend
npm install
npm run build
exec "$@"
