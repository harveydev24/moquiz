from rest_framework import serializers
from ..models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Article
        fields = '__all__'


class ArticleLikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class CommentSerializer(serializers.ModelSerializer):
        username = serializers.CharField(source='user.username')

        class Meta:
            model = Comment
            fields = '__all__'

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):

    class CommentSerializer(serializers.ModelSerializer):
        username = serializers.CharField(source='user.username')

        class Meta:
            model = Comment
            fields = '__all__'

    comments = CommentSerializer(many=True, read_only=True)

    username = serializers.CharField(source='user.username')
    
    class Meta:
        model = Article
        fields = '__all__'


