from django.shortcuts import render
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
    try:
        question = Question.objects.get(pk = question_id)
    except Question.does_not_exist:
        raise Http404("Question does not exist");

    choices = question.choice_set.all()
    return render(request, "polls/detail.html", 
                  {
                      "choice_list" : choices
                    })
