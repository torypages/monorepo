from typing import Union

from rest_framework.decorators import api_view
from rest_framework.response import Response

from app1.models import Person
from app1.tasks import hello_task


def person_to_dict(person: Person) -> dict[str, Union[int, str]]:
    return {
        "id": person.id,
        "name": person.name,
        "created_at": str(person.created_at),
    }


@api_view(["GET", "POST"])
def hello_view(_):
    people = [person_to_dict(person) for person in Person.objects.all().order_by("-id")]
    hello_task.apply_async()
    return Response({"people": people})
