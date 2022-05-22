from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import *

import requests
from bs4 import BeautifulSoup

from .models import *
from .serializers.article import ArticleSerializer, ArticleLikeSerializer, ArticleDetailSerializer
# Create your views here.

User = get_user_model()
home_data = None


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
        serializer = ArticleDetailSerializer(article)
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
    serializer = ArticleLikeSerializer(article)
    return Response(serializer.data, status=HTTP_200_OK)


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


@api_view(['GET'])
def home(request):
    global home_data

    if home_data != None:
        return Response(home_data, status=HTTP_200_OK)

    url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
    response = requests.get(url).text
    movies = {'data': []}
    doc = BeautifulSoup(response, 'html.parser')
    doc = doc.select_one(
        '#contents > div.wrap-movie-chart > div.sect-movie-chart')
    docs = doc.findAll('ol')
    for i in range(len(docs)):
        doc = docs[i]
        for content in doc.findAll('li'):
            image = content.find('div', {'class': 'box-image'})
            result = content.find('div', {'class': 'box-contents'})
            movie_url = 'http://www.cgv.co.kr'+result.select_one('a')['href']

            if result:
                response = requests.get(movie_url).text
                doc_detail = BeautifulSoup(response, 'html.parser')
                reservation_link = doc_detail.select_one(
                    '#select_main > div.sect-base-movie > div.box-contents > span.like > a')['href']
                director = doc_detail.select_one(
                    '.spec > dl > dd').get_text().strip()

                actors = [actor.get_text()
                          for actor in doc_detail.select('.spec > dl > dd.on > a')]

                overview = ' '.join(doc_detail.select_one(
                    '.sect-story-movie').get_text().split())

                movies['data'].append({'title': result.select_one('strong').text, 'image': image.select_one('img')[
                    'src'], 'percent': result.select_one('span').text, 'url': movie_url, 'director': director, 'actors': actors, 'overview': overview})

    home_data = movies['data']

    return Response(movies['data'], status=HTTP_200_OK)
