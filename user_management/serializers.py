from rest_framework import serializers
from user_management.models import User
from package.serializers import LikedSerializer

class UserSerializer(serializers.ModelSerializer):   
    liked_packages = LikedSerializer(many=True, read_only=True) 
    class Meta:
        model = User
        fields = ['id', 'username', 'password','email', 'liked_packages']