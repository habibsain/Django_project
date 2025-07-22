from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.index, name = "index"),
    #path("", views.IndexView.as_view(), name = "index"),
    path("<int:question_id>/", views.detail, name = "detail"),
    #path("<int:pk>/", views.DetailView.as_view(), name = "detail"),
    path("<int:question_id>/vote/", views.vote, name = "vote"),
    path("<int:question_id>/result/", views.result, name = "result"),
    # path("<int:question_id>/result/", views.ResultView.as_view(), name = "result"),

    #add new question
    path("new/", views.add_page, name = "add"),

    #edit choice
    path("<int:question_id>/edit_page/", views.edit_page, name = "edit_page"),
    path("add/", views.add_question, name = "add_question"),
    path("<int:choice_id>/delete_choice", views.delete_choice, name = "delete_choice"),
    path("<int:question_id>/edit_choice", views.edit_choice, name = "edit_choice"),
    path("<int:question_id>/add_choice", views.add_choice, name = "add_choice"),
    path("<int:question_id>/change_question", views.change_question, name = "change_question"),
    path("<int:question_id>/edit_question/", views.edit_question, name = "edit"),
]
