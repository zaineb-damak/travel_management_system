from rest_framework import serializers
from .models import Booking
from user_management.serializers import UserSerializer
from package.serializers import PackageSerializer

class BookingSerializer(serializers.ModelSerializer):
    package = PackageSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'package', 'status','booking_date']