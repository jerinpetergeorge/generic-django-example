import typing

from strawberry import django as strawberry_django

from ..models import Choice, Poll


@strawberry_django.type(model=Poll)
class PollType:
    id: int
    question: str
    choices: typing.List["ChoiceType"]


@strawberry_django.type(model=Choice)
class ChoiceType:
    id: int
    poll: PollType
    choice_text: str
    votes: int
