from django.urls import path
from booking import views

urlpatterns = [
path('bookings/', views.BookingList.as_view(), name='booking-list'),
path('bookings/<int:pk>/', views.BookingDetail.as_view(), name='booking-detail'),
path('packages/<int:pk>/book/', views.BookingCreate.as_view(), name='book-package'),
path('bookings/<int:pk>/', views.BookingDestroy.as_view(), name='booking-delete'),
]