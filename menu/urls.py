from django.urls import path
from . import views

urlpatterns = [
    path('menus/', views.MenuList.as_view(), name='menus'),
]