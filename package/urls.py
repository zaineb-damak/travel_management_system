from django.urls import path
from package import views

urlpatterns = [
path('packages/', views.PackageList.as_view(), name='package-list'),
path('packages/<int:pk>/', views.PackageDetail.as_view(), name='package-detail'),
path('days/', views.DayList.as_view(), name='day-list'),
path('days/<int:pk>/', views.DayDetail.as_view(), name='day-detail'),
path('liked/', views. LikedList.as_view(), name='liked-list'),
path('packages/<int:pk>/liked/', views.LikedCreate.as_view(), name='like-package'),
]
