from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers.ranking import RankingSerializer

User = get_user_model()

# Create your views here.


@api_view(['GET'])
def ranking(request):
    rankers = User.objects.all().order_by('-score')[:10]
    serializer = RankingSerializer(rankers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def score(request):
    user = request.user
    data = request.data

    user.score += data['score']
    user.correct += data['correct']
    user.wrong += data['wrong']

    user.save()

    ret = {
        'score': user.score,
        'correct': user.correct,
        'wrong': user.wrong
    }

    return Response(ret)
