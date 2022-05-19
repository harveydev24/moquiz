from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers.article import ArticleSerializer
# Create your views here.

User = get_user_model()


@api_view(['GET'])
def index(request):
    articles = Article.objects.order_by('-pk')[:10]
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def article_create(request):

    article = Article()
    article.user = request.user
    article.title = request.data['title']
    article.content = request.data['content']

    article.save()
    return Response({'pk': article.pk})


@api_view(['GET', 'POST', 'DELETE'])
def article(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'POST':

        article.title = request.data['title']
        article.content = request.data['content']
        article.save()

        return HttpResponse()

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse()


@api_view(['POST'])
def article_like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    user = request.user
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)
    return HttpResponse()


@api_view(['POST'])
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment = Comment()

    comment.user = request.user
    comment.article = article
    comment.content = request.data['content']

    comment.save()
    return HttpResponse()


@api_view(['DELETE'])
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return HttpResponse()
