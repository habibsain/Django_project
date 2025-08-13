from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Question(models.Model):
    question_text = models.TextField(max_length=100, unique=True)
    pub_date = models.DateTimeField("Date published")
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return (self.pub_date >= timezone.now() - datetime.timedelta(days=1)) and (self.pub_date <= timezone.now())

    

class Choice(models.Model):
    choice_text = models.TextField(max_length=100)
    vote = models.IntegerField()
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    def __str__(self):
        return self.choice_text
