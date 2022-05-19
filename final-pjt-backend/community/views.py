from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import *

from .models import *
from .serializers.article import ArticleSerializer
# Create your views here.

User = get_user_model()


@api_view(['GET'])
def index(request):
    articles = Article.objects.order_by('-pk')[:10]
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
def article_create(request):

    article = Article()
    article.user = request.user
    article.title = request.data['title']
    article.content = request.data['content']

    article.save()
    return Response({'pk': article.pk}, status=HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def article(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=HTTP_200_OK)

    elif request.method == 'PUT':
        if request.user == article.user:
            article.title = request.data['title']
            article.content = request.data['content']
            article.save()
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=HTTP_200_OK)


@api_view(['POST'])
def article_like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    user = request.user
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)
    return Response(status=HTTP_200_OK)


@api_view(['POST'])
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment = Comment()

    comment.user = request.user
    comment.article = article
    comment.content = request.data['content']

    comment.save()
    return Response(status=HTTP_201_CREATED)


@api_view(['DELETE'])
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response(status=HTTP_200_OK)
