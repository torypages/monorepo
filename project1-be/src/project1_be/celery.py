from __future__ import absolute_import

import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()

# TODO: string "project1_be" should be taken from a central place
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1_be.settings")

celery_broker = (
    "amqp://{celery_broker_user}:{celery_broker_password}@"
    "{celery_broker_host}:{celery_broker_port}/{celery_broker_vhost}"
).format(
    celery_broker_user=os.environ["celery_broker_user"],
    celery_broker_password=os.environ["celery_broker_password"],
    celery_broker_host=os.environ["celery_broker_host"],
    celery_broker_port=os.environ["celery_broker_port"],
    celery_broker_vhost=os.environ["celery_broker_vhost"],
)

print("-" * 88)
print(f"Connecting to broker with: {celery_broker}")

app = Celery(
    "test_celery",
    broker=celery_broker,
    backend="rpc://",
    include=["app1.tasks"],
)
