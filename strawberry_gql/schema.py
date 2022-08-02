import typing

import strawberry

from polls.strawberry.schema import PollQueries

from .resolvers import get_books
from .types import BookType


@strawberry.type
class Query(
    PollQueries,
):
    ...
    books: typing.List[BookType] = strawberry.field(resolver=get_books)


# @strawberry.type
# class Mutation(
# ):
#     ...
schema = strawberry.Schema(
    query=Query,
    # mutation=Mutation,
)
