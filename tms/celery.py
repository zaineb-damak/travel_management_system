from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tms.settings')
celery = Celery('tasks', broker='amqp://guest@localhost//')

app = Celery('tms')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()