import pytest

from polls.models import Poll

pytestmark = pytest.mark.django_db


def test_add():
    assert 1 + 1 == 2


@pytest.mark.django_db
class TestPolls:
    pytestmark = pytest.mark.django_db

    def test_polls_create(self):
        poll = Poll.objects.create(question="Test")
        assert poll.pk
