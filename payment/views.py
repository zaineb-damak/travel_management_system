from rest_framework import generics
from payment.models import Payment
from payment.serializers import PaymentSerializer
from booking.models import Booking
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime


class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    page_size = 10

class PaymentDetail(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    page_size = 10

class PaymentCreate(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        try:
            booking = Booking.objects.get(pk=self.kwargs.get('pk'))
        except Booking.DoesNotExist:
            return Response({"error": "Booking does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        request.data['booking'] = booking.id
        request.data['payment_date'] = datetime.now().date()  
        request.data['amount'] = booking.package.price        
        
        return super().create(request, *args, **kwargs)