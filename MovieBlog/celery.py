import os

from celery import Celery
from celery import shared_task


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
	'MovieBlog.settings')

app = Celery('MovieBlog')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
