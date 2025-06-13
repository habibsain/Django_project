from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:question_id>/", views.detail, name = "detail"),
    path("<int:question_id>/vote/", views.vote, name = "vote"),
    path("<int:question_id>/result/", views.result, name = "result"),
    path("new/", views.add_page, name = "add"),
    path("add/", views.add_question, name = "add_question"),
    path("<int:question_id>/choice_page", views.choice_page, name = "choice_page"),
    path("<int:question_id>/add_choice", views.add_choice, name = "add_choice"),
]
