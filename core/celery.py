import os

from celery import Celery
from kombu import Queue

# set the default django settings to celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.base")

# Define queues
task_queues = (Queue("quronapp_queue", routing_key="quronapp_queue"),)


app = Celery("celery")

app.config_from_object("django.conf:settings")

app.conf.task_queues = task_queues

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# message broker configurations
BASE_REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
