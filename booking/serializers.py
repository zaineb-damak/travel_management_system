from rest_framework import serializers
from .models import Booking
from user_management.serializers import UserSerializer
from package.serializers import PackageSerializer

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    trip_package = PackageSerializer()

    class Meta:
        model = Booking
        fields = ['id', 'user', 'trip_package', 'status','booking_date']