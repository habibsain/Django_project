from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import *

# Create your views here.
def index(request):
    question_list = Question.objects.all()
    return render(request, "polls/index.html", 
                  {
                      "question_list" : question_list
                    })

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    choices = question.choice_set.all()
    return render(request, "polls/detail.html", 
                  {
                      "choice_list" : choices
                    })

def vote(request, question_id):
    pass
