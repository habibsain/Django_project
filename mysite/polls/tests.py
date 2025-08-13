from django.test import TestCase
from django.utils import timezone
import datetime 

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recentlly(self):
        time = timezone.now() + datetime.timedelta(days=30) # pub date is 30 days in future
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)