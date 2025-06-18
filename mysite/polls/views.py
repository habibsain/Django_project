from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.utils import timezone
from .models import Question, Choice

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

        return HttpResponseRedirect(reverse( "polls:result", args = (question.id,)))#The comma in args is important as it gives args value a list instead of a single value
    #Note: problem of implicit type conversion

def result(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/result.html",
                  {
                      "question": question
                      })

def add_page(request):

    return render(request, "polls/add_question.html")

def add_question(request):
    #Todo:
    #url:ok
    #link with index:OK
    #form to post new question:Ok
    #choices for the question as well:ok
    #update the new question from result.POST to database:OK
    

    q = Question(question_text = request.POST["question"], pub_date = timezone.now())
    q.save()

    return HttpResponseRedirect(reverse("polls:add"))

def edit_page(request):
    pass

def choice_page(request, question_id):
    #Todo:
    #url-edit pass:ok
    pass

def add_choice(request, question_id):
    pass
