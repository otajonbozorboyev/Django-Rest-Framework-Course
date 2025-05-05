from rest_framework import serializers
from .models import BookBanner, Video, Podcast, Book, Language, Level, Unit


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'image2', 'price')


class LanguageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'image2', 'price', 'description', 'rating')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'name', 'units_count')

    units_count = serializers.SerializerMethodField()

    @staticmethod
    def get_units_count(obj):
        return obj.units.count()


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'name')


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