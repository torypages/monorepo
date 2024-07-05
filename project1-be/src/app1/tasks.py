import random
import string

from celery import shared_task

from app1.models import Person


def random_chars(n: int) -> str:
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(n)
    )


@shared_task()
def hello_task():
    if Person.objects.count() > 10:
        Person.objects.filter(id__gt=-1).delete()

    person = Person(name=random_chars(22))
    person.save()
