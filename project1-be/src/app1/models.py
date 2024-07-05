from django.db import models
from django.utils.timezone import now


class Person(models.Model):
    id: int
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=now())
