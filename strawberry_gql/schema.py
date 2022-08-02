import typing

import strawberry

from .resolvers import get_books
from .types import Book


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)


# @strawberry.type
# class Mutation(
# ):
#     ...
schema = strawberry.Schema(
    query=Query,
    # mutation=Mutation,
)
