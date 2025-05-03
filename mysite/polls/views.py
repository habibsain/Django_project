from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def detail(request, question_id):
    question = Question.objects.get(pk = question_id)
    quest_t = question.question_text
    return HttpResponse(quest_t)