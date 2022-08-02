import typing

import strawberry
from strawberry import django as strawberry_django

from .types import PollType


@strawberry.type
class PollQueries:
    polls: typing.List[PollType] = strawberry_django.field()
