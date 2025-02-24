from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("question/<int:question_id>/", views.question, name="question"),
    path("random/", views.random_question, name="random_question")
]