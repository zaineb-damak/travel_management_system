from rest_framework import serializers
from user_management.models import User

class UserSerializer(serializers.ModelSerializer):   
       
    class Meta:
        model = User
        fields = ['id', 'username', 'password','email']