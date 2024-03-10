import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm_django.settings")

app = Celery("crm_django")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

# можно тут настройки оставить, либо общие в settings.py
app.conf.beat_schedule = {
    "update_contracts_validity": {
        "task": "contracts.tasks.check_validity_contracts",
        "schedule": crontab(
            hour="0", minute="0"
        ),  # Задача будет выполняться ежедневно в полночь
    },
}
