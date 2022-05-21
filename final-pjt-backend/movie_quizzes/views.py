from django.contrib.auth import get_user_model
from django.db.models import Max

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import *
from .models import *

import random

# Create your views here.

User = get_user_model()

movies_have_images = ['내부자들', '베테랑', '아저씨', '부당거래', '신세계']


@api_view(['GET'])
def quiz(request):
    # 문제 개수
    n = 12
    ret = {'quizzes': []}

    # 최대 인덱스 찾기
    actor_max_pk = Actor.objects.all().aggregate(
        actor_max_pk=Max("pk"))['actor_max_pk']
    movie_max_pk = Movie.objects.all().aggregate(
        movie_max_pk=Max("pk"))['movie_max_pk']
    line_max_pk = Famous_Line.objects.all().aggregate(
        line_max_pk=Max("pk"))['line_max_pk']

    # 영화제목 초성
    movie_pks = random.sample(range(1, movie_max_pk), 3)
    for movie_pk in movie_pks:
        movie = Movie.objects.get(pk=movie_pk)
        ret['quizzes'].append({
            'type': 1,
            'problem': movie.title_initial,
            'answer': movie.title
        })

    # 명대사 초성
    line_pks = random.sample(range(1, line_max_pk), 3)
    for line_pk in line_pks:
        line = Famous_Line.objects.get(pk=line_pk)
        ret['quizzes'].append({
            'type': 2,
            'problem': line.line_initial,
            'answer': line.line,
            'title': line.movie.title
        })

    # 다음 대사는 어떤 영화에 나온 대사인가?
    line_pks = random.sample(range(1, line_max_pk), 2)
    for line_pk in line_pks:
        line = Famous_Line.objects.get(pk=line_pk)
        ans = line.movie.title
        option = [ans]
        while len(option) < 4:
            tmp_movie_pk = random.randint(1, movie_max_pk)
            movie = Movie.objects.get(pk=tmp_movie_pk)
            if movie.title not in option:
                option.append(movie.title)
        random.shuffle(option)
        ret['quizzes'].append(
            {'type': 3, 'problem': line.line, 'answer': ans, 'option': option})

    # 이미지 퀴즈
    for _ in range(2):
        img_idx = random.sample(range(5), 2)
        movie1 = Movie.objects.get(title=movies_have_images[img_idx[0]])
        movie2 = Movie.objects.get(title=movies_have_images[img_idx[1]])
        img1 = Movie_Image.objects.filter(movie=movie1.pk)
        img2 = Movie_Image.objects.filter(movie=movie2.pk)
        img1_idx = random.sample(range(8), 3)
        img2_idx = random.randint(0, 7)

        img_src = []
        for idx in img1_idx:
            img_src.append(img1[idx].image_url)
        img_src.append(img2[img2_idx].image_url)
        random.shuffle(img_src)
        ret['quizzes'].append(
            {'type': 4, 'img_src': img_src, 'answer': img2[img2_idx].image_url})

    random.shuffle(ret['quizzes'])

    return Response(ret, status=HTTP_200_OK)
