from django.urls import path, include

urlpatterns = [
    path('lang/', include('lang.urls')),
    path('user/', include('user.urls'))
]