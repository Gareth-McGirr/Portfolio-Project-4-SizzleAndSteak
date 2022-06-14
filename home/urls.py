from django.urls import path
from home.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home')
    ]
