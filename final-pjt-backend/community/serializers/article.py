from rest_framework import serializers
from ..models import Article


class ArticleSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    
    class Meta:
        model = Article
        fields = '__all__'


