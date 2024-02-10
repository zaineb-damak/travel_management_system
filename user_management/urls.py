from django.urls import path
from user_management import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

urlpatterns = [
path('users/', views.UserList.as_view(), name='user-list'),
path('users/register', views.UserCreate.as_view(), name='user-create'),
path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('users/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]