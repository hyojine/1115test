from rest_framework import serializers

from articles.models import Article as ArticleModel


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields= "__all__"