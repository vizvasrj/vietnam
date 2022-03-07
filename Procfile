release: python manage.py migrate
web: gunicorn china.wsgi --log-file=-
worker: celery --app china worker -l info