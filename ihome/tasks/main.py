# coding=utf8
from celery import Celery
from ihome.tasks import config

app = Celery('ihome')

app.config_from_object(config)

app.autodiscover_tasks(['ihome.tasks.sms'])
