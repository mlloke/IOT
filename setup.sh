#!/bin/bash
set -e
DB_NAME=${1:-iotproject}
DB_USER=${2:-iotprojectuser}
DB_USER_PASS=${3:-password}
sudo -u postgres -H createdb  $DB_NAME;
sudo -u postgres -H psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_USER_PASS';"
sudo -u postgres -H psql -c "alter role $DB_USER set client_encoding to 'utf8';"
sudo -u postgres -H psql -c "alter role $DB_USER set default_transaction_isolation to 'read committed';"
sudo -u postgres -H psql -c "alter role $DB_USER set timezone to 'UTC';"
sudo -u postgres -H psql -c "grant all privileges on database $DB_NAME to $DB_USER;"
echo "Postgres User '$DB_USER' and database '$DB_NAME' created."

#setup Django postgres
pip install psycopg2==2.8.6
pip install django-widget-tweaks
pip install djangorestframework
pip install pygments
echo "Django psycopg2, widget-tweaks, json-editor installed."


cd /home/ubuntu/mysite


#django project make migrations
pip install django-jsoneditor
#python3 -m pip install Django==3.1
#python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
