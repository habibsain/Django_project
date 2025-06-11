from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse

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
                      "choice_list" : choices,
                      "question" : question
                    })

def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    try:
        selected_choice = question.choice_set.get( pk=request.POST["choice"])

    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", 
                {
                "question" : question,
                "choice_list" : choices
                })
                
    else:
        selected_choice.vote = F("vote") + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse( "polls:results", args = (question_id)))

def result(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/result.html",
                  {
                      "question": question
                      })
