from django.test import TestCase

from ..models import Choice, Poll


class PollsTest(TestCase):
    def test_polls(self):
        poll = Poll.objects.create(question="What's your favorite color?")
        self.assertEqual(poll.question, "What's your favorite color?")
        choice = Choice.objects.create(poll=poll, choice_text="Blue")
        self.assertEqual(choice.choice_text, "Blue")
        self.assertEqual(choice.poll, poll)
