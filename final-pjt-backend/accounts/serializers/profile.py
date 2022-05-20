from rest_framework import serializers
from django.contrib.auth import get_user_model


class ProfileSerializer(serializers.ModelSerializer):
    followings_cnt = serializers.IntegerField(
        source='followings.count', read_only=True)
    followers_cnt = serializers.IntegerField(
        source='followers.count', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'nickname', 'score', 'correct',
                  'wrong', 'followings_cnt', 'followers_cnt')
