from django.urls import path
from . import views

urlpatterns = [  
    path('createbooking/', views.CreateBookingView.as_view(), name='createbooking'),
    path('managebookings/', views.BookingsList.as_view(), name='managebookings'),
]
