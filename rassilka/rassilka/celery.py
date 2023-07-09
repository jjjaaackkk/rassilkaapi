from celery import Celery
import os
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rassilka.settings')
 
app = Celery('rassilka')
app.conf.enable_utc = False
app.conf.update(timezone = 'Europe/Moscow')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'campaigns': {
        'task': 'core.task.init_job',
        'schedule': crontab(minute='*/1'),
        #'args': '',
    }
}

app.autodiscover_tasks()