from user_management.models import User
from user_management.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserList(generics.ListAPIView):
    queryset  = User.objects.all()
    serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView):
    queryset  = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
            

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

  

