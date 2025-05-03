from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),

    #check for invalid question id later
    path("<int:question_id>/", views.detail, name="detail"),
]