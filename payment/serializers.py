from rest_framework import serializers
from payment.models import Payment
from booking.serializers import BookingSerializer

class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = ['id', 'booking', 'credit_card', 'pin','amount', 'payment_date']