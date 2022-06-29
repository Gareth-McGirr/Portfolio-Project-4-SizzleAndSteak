from django.urls import path
from . import views

urlpatterns = [
    path(
        'menus/', views.MenuListView.as_view(), name='menus'
        ),
    path(
        'createmenu/', views.CreateMenuView.as_view(), name='createmenu'
        ),
    path(
        'editmenu/<slug:pk>/', views.EditMenuView.as_view(), name='editmenu'
        ),
    path(
        'managemenus/', views.ManageMenusListView.as_view(), name='managemenus'
        ),
    path(
        'delete/<slug:pk>/', views.DeleteMenuView.as_view(), name="delete_menu"
        )
]
