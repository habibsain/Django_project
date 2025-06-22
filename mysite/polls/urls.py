from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name = "index"),
    path("<int:pk>/", views.DetailView.as_view(), name = "detail"),
    path("<int:pk>/vote/", views.vote, name = "vote"),
    path("<int:question_id>/result/", views.ResultView.as_view(), name = "result"),
    path("new/", views.add_page, name = "add"),
    path("add/", views.add_question, name = "add_question"),
    path("<int:question_id>/choice_page", views.choice_page, name = "choice_page"),
    path("<int:question_id>/add_choice", views.add_choice, name = "add_choice"),
    path("<int:question_id>/change_question", views.change_question, name = "change_question"),
    path("edit_page/", views.edit_page, name = "edit_page"),
    path("<int:question_id>/edit_question", views.edit_question, name = "edit"),
]
