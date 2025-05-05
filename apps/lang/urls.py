from django.urls import path
from .views import (
    BookBannerAPIView, 
    VideoBannerAPIView, 
    PodcastBannerAPIView, 
    VideoAPIView, 
    PodcastAPIView,
    BookAPIView, 
)

urlpatterns = [
    path("book-banner/", BookBannerAPIView.as_view(), name="book_banner"),
    path("video-banner/", VideoBannerAPIView.as_view(), name="video_banner"),
    path("podcast-banner/", PodcastBannerAPIView.as_view(), name="podcast_banner"),
    path("videos/<int:language_id>/", VideoAPIView.as_view(), name="videos"),
    path("podcasts/<int:language_id>/", PodcastAPIView.as_view(), name="podcasts"),
    path("books/<int:language_id>/", BookAPIView.as_view(), name="books"),
]