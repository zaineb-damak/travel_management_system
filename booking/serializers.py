from rest_framework import serializers
from .models import Booking
from user_management.serializers import UserSerializer
from package.serializers import PackageSerializer

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        status = serializers.CharField(default='Pending')
        fields = ['id', 'user', 'package', 'status','booking_date']