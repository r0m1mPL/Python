from celery import Celery
from celery.schedules import crontab


app = Celery('celery_beat', broker='redis://localhost:6379/0', include=['tasks'])

app.conf.beat_schedule = {
    'clear_tmp': {
        'task': 'tasks.clear_tmp',
        'schedule': crontab(minute=0, hour=4),
    },
}

app.conf.timezone = 'UTC'

app.autodiscover_tasks()
