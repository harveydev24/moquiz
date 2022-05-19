from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'movie_quizzes'

urlpatterns = [
    path('quiz/', views.quiz),
]
