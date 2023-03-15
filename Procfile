web gunicorn Sheraz_aziz_project.wsgi:application --log-file -
python manage.py collectstatic --noinput
manage.py makemigrations
manage.py migrate
heroku config:set DEBUG_COLLECTSTATIC=1