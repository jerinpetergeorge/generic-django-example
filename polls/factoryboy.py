import factory
from factory.django import DjangoModelFactory

from .models import Choice, Poll


class PollFactory(DjangoModelFactory):
    class Meta:
        model = Poll

    question = factory.Faker("sentence")


class ChoiceFactory(DjangoModelFactory):
    class Meta:
        model = Choice

    choice_text = factory.Faker("first_name")
    votes = factory.Faker("random_int", min=0, max=100)


def create_polls(polls: int, choices: int):
    for _poll in range(polls):
        poll: Poll = PollFactory()
        for _choice in range(choices):
            ChoiceFactory(poll=poll)
    return Poll.objects.all()
