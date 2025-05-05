from rest_framework import generics
from .serializers import (
    VideoPodcastBannerSerializer, 
    BookBannerSerializer, 
    VideoSerializer, 
    PodcastSerializer,
    BookSerializer, 
)
from .models import VideoBanner, PodcastBanner, BookBanner, Video, Podcast, Book


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


