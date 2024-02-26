from django.urls import path
from package import views

urlpatterns = [
path('packages/', views.PackageList.as_view(), name='package-list'),
path('packages/<int:pk>/', views.PackageDetail.as_view(), name='package-detail'),
path('days/', views.DayList.as_view(), name='days-list'),
path('days/<int:pk>/', views.DayDetail.as_view(), name='day-detail'),
path('hotels/', views.HotelList.as_view(), name='hotels-list'),
path('hotels/<int:pk>/', views.HotelDetail.as_view(), name='hotle-detail'),
path('liked/', views. LikedList.as_view(), name='liked-list'),
path('packages/<int:pk>/liked/', views.LikedCreate.as_view(), name='like-package'),
]
