from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    question_list = Question.objects.all()
    return render(request, "polls/index.html", 
                  {
                      "question_list" : question_list
                    })

def detail(request, question_id):
    question = Question.objects.get(pk = question_id)
    quest_t = question.question_text
    return HttpResponse(quest_t)