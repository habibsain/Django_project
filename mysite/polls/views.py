from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice

#Create your views here.
def index(request):
    question_list = Question.objects.all()
    return render(request, "polls/index.html", 
                  {
                      "question_list" : question_list
                    })

# class IndexView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "question_list"

#     def get_queryset(self):
#         return Question.objects.order_by('question_text', 'pub_date').distinct('question_text')


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    choices = question.choice_set.all()
    return render(request, "polls/detail.html", 
                  {
                      "choice_list" : choices,
                      "question" : question
                    })
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "polls/detail.html"

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

        return HttpResponseRedirect(reverse( "polls:result", args = (question.id,)))
        #The comma in args is important as it gives args value a list instead of a single value
        #Note: problem of implicit type conversion

def result(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/result.html",
                  {
                      "question": question
                      })

# class ResultView(generic.DetailView):
#     model = Question

#     template_name = "polls/result.html"


def add_page(request):

    return render(request, "polls/add_question.html")

def add_question(request):
    #Todo:
    #url:ok
    #link with index:OK
    #form to post new question:Ok
    #choices for the question as well:ok
    #update the new question from result.POST to database:OK
    
    # try:
    q = Question(question_text = request.POST["question"], pub_date = timezone.now())
    # except(IntegrityError):

    q.save()
    print(q.id)
    # except: 

    return HttpResponseRedirect(reverse("polls:edit_choice", args = (q.id,)))

def edit_page(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    choices = question.choice_set.all()
    return render(request, "polls/edit_page.html", 
                  {
                      "choice_list" : choices,
                      "question" : question
                    })



def edit_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    
    return HttpResponseRedirect(reverse( "polls:index"))

def change_question(request, question_id):
    pass

def delete_choice(request, choice_id):
    #Todo:
    #url-edit pass:ok
    choice = get_object_or_404(Choice, pk=choice_id)
    choice.delete()
    return HttpResponseRedirect(reverse( "polls:index"))


def edit_choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/edit_choice.html", 
                  {
                      "question" : question
                    })

def add_choice(request, question_id):
    q = Question.objects.get(pk=question_id)
    q.choice_set.create(choice_text = request.POST["choice_text"], vote = 0)

    return HttpResponseRedirect(reverse("polls:edit_choice", args = (q.id,)))


