from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import *

from .serializers.ranking import RankingSerializer
from .serializers.profile import ProfileSerializer

User = get_user_model()

# Create your views here.


@api_view(['GET'])
def ranking(request):
    rankers = User.objects.all().order_by('-score')[:10]
    serializer = RankingSerializer(rankers, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['PUT'])
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

    return Response(ret, status=HTTP_200_OK)


@api_view(['GET'])
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)


@api_view(['PUT'])
def follow(request, pk):
    target_user = get_object_or_404(User, pk=pk)
    user = request.user
    if target_user.followers.filter(pk=user.pk).exists():
        target_user.followers.remove(user)
    else:
        target_user.followers.add(user)
    return Response(statue=HTTP_200_OK)
