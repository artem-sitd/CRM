import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
from celery.schedules import crontab, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_django.settings')

app = Celery('crm_django')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # 'update_contracts_validity': {
    #     'task': 'contracts.tasks.check_validity_contracts',
    #     'schedule': crontab(hour='0', minute='0'),  # Задача будет выполняться ежедневно в полночь
    # },
    'task5sec': {
        'task': 'contracts.tasks.task5_seconds',
        'schedule': 5.0,
    },
    'task10sec': {
        'task': 'contracts.tasks.task10_seconds',
        'schedule': timedelta(seconds=10)
    }
}
