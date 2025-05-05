from django.urls import path
from .views import (
    UserInfoAPIView, 
    PaymentHistoryView, 
    MyLanguageAPIView, 
    MyLevelAPIView, 
    MyUnitAPIView,
    MyUnitDetailAPIView, 
    VocabAPIView, 
    PhraseAPIView
)

urlpatterns = [
    path('user/', UserInfoAPIView.as_view()),
    path('payment-history/', PaymentHistoryView.as_view()),
    path('my-languages/', MyLanguageAPIView.as_view()),
    path('my-levels/<int:language_id>/', MyLevelAPIView.as_view()),
    path('my-units/<int:level_id>/', MyUnitAPIView.as_view()),
    path('my-unit-detail/<int:pk>/', MyUnitDetailAPIView.as_view()),
    path('vocab/<int:unit_id>/', VocabAPIView.as_view()),
    path('phrase/<int:unit_id>/', PhraseAPIView.as_view()),
]