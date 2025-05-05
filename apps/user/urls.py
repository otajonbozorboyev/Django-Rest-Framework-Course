from django.urls import path
from .views import (
    UserInfoAPIView, 
    PaymentHistoryView, 
)

urlpatterns = [
    path('user/', UserInfoAPIView.as_view()),
    path('payment-history/', PaymentHistoryView.as_view()),
]