from django.urls import path
from .views import (
    BookBannerAPIView, 
    VideoBannerAPIView, 
    PodcastBannerAPIView, 
)

urlpatterns = [
    path("book-banner/", BookBannerAPIView.as_view(), name="book_banner"),
    path("video-banner/", VideoBannerAPIView.as_view(), name="video_banner"),
    path("podcast-banner/", PodcastBannerAPIView.as_view(), name="podcast_banner"),
]