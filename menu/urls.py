from django.urls import path
from . import views

urlpatterns = [
    path('menus/', views.MenuListView.as_view(), name='menus'),
    path('createmenu/', views.CreateMenuView.as_view(), name='createmenu'),
]