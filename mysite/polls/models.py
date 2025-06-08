from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.TextField(max_length=100)
    pub_date = models.DateField("Date published")
    
    def __str__(self):
        return self.question_text

    

class choice(models.Model):
    choice_text = models.TextField(max_length=100)
    vote = models.IntegerField()
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    def __str__(self):
        return self.choice_text
