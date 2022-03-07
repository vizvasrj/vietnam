release: python manage.py migrate
web: gunicorn vietnam.wsgi --log-file=-
worker: celery --app vietnam worker -l info