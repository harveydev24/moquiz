from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('article/', views.article_create, name='article_create'),
    path('article/<int:pk>/', views.article, name='article'),
    path('article/<int:pk>/like', views.article_like, name='article_like'),
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/',
         views.comment_delete, name='comment_delete'),
]
