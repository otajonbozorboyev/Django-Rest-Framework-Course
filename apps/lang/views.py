from rest_framework import generics
from .serializers import (
    VideoPodcastBannerSerializer, 
    BookBannerSerializer, 
    VideoSerializer, 
    PodcastSerializer,
    BookSerializer, 
    LanguageSerializer, 
    LanguageDetailSerializer, 
    LevelSerializer, 
    UnitSerializer
)
from .models import VideoBanner, PodcastBanner, BookBanner, Video, Podcast, Book, Language, Level, Unit


class LanguageListAPIView(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageDetailAPIView(generics.RetrieveAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageDetailSerializer


class LevelListAPIView(generics.ListAPIView):
    serializer_class = LevelSerializer

    def get_queryset(self):
        return Level.objects.filter(language_id=self.kwargs['language_id'])


class UnitListAPIView(generics.ListAPIView):
    serializer_class = UnitSerializer

    def get_queryset(self):
        return Unit.objects.filter(level_id=self.kwargs['level_id'])


class VideoBannerAPIView(generics.ListAPIView):
    queryset = VideoBanner.objects.all()
    serializer_class = VideoPodcastBannerSerializer


class PodcastBannerAPIView(generics.ListAPIView):
    queryset = PodcastBanner.objects.all()
    serializer_class = VideoPodcastBannerSerializer


class BookBannerAPIView(generics.ListAPIView):
    queryset = BookBanner.objects.all()
    serializer_class = BookBannerSerializer


class VideoAPIView(generics.ListAPIView):
    def get_serializer_class(self):
        return VideoSerializer

    def get_queryset(self):
        return Video.objects.filter(language_id=self.kwargs['language_id'])


class PodcastAPIView(generics.ListAPIView):
    serializer_class = PodcastSerializer

    def get_queryset(self):
        return Podcast.objects.filter(language_id=self.kwargs['language_id'])


class BookAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        qs = Book.objects.filter(language_id=self.kwargs['language_id'])
        level_id = self.request.query_params.get('level_id', None)
        if level_id:
            qs = qs.filter(level_id=level_id)
        return qs
