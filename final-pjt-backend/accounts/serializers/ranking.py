from rest_framework import serializers
from django.contrib.auth import get_user_model


class RankingSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'nickname', 'score', 'correct', 'wrong',)
