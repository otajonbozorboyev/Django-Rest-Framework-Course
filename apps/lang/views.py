from rest_framework import generics
from .serializers import VideoPodcastBannerSerializer, BookBannerSerializer
from .models import VideoBanner, PodcastBanner, BookBanner


class VideoBannerAPIView(generics.ListAPIView):
    queryset = VideoBanner.objects.all()
    serializer_class = VideoPodcastBannerSerializer


class PodcastBannerAPIView(generics.ListAPIView):
    queryset = PodcastBanner.objects.all()
    serializer_class = VideoPodcastBannerSerializer


class BookBannerAPIView(generics.ListAPIView):
    queryset = BookBanner.objects.all()
    serializer_class = BookBannerSerializer
