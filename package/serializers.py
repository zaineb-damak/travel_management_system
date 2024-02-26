from rest_framework import serializers
from .models import Package, Day, Liked, Hotel

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['id', 'title', 'content','package_id']
        
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'title','package_id']

class PackageSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True, read_only=True) 
    class Meta:
        model = Package
        fields = ['id', 'destination', 'duration', 'price', 'days']

class LikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liked
        fields = ['id', 'user', 'package']