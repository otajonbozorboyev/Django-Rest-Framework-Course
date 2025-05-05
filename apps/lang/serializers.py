from rest_framework import serializers
from .models import BookBanner, Video, Podcast, Book


class BookBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookBanner
        fields = ('title', 'image', 'pages', 'coin')


class VideoPodcastBannerSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    time = serializers.CharField()
    coin = serializers.IntegerField()


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'poster', 'video')


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ('title', 'image', 'audio')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'image', 'pdf')



