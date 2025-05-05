from rest_framework import serializers
from .models import BookBanner


class BookBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookBanner
        fields = ('title', 'image', 'pages', 'coin')


class VideoPodcastBannerSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    time = serializers.CharField()
    coin = serializers.IntegerField()




