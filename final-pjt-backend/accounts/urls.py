from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('ranking/', views.ranking),
    path('score/', views.score),
    path('profile/<username>/', views.profile),
    path('<int:pk>/follow/', views.follow),
    path('all/', views.all_user)
]
