from user_management.models import User
from user_management.serializers import UserSerializer
from rest_framework import generics

class UserList(generics.ListAPIView):
    queryset  = User.objects.all()
    serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView):
    queryset  = User.objects.all()
    serializer_class = UserSerializer
            

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

