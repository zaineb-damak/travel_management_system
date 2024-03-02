from rest_framework import generics
from payment.models import Payment
from payment.serializers import PaymentSerializer
from booking.models import Booking
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from payment.tasks import send_email
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class PaymentList(generics.ListAPIView):
    serializer_class = PaymentSerializer
    page_size = 10
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Payment.objects.all().filter(booking__user=self.request.user)
        return queryset

class PaymentDetail(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    page_size = 10
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = Payment.objects.all().filter(booking__user=self.request.user)
        return queryset

class PaymentCreate(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            booking = Booking.objects.get(pk=self.kwargs.get('pk'))
        except Booking.DoesNotExist:
            return Response({"error": "Booking does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        user_email = booking.user.email
        user_name = booking.user.username

        booking_id = booking.id
        package_id = booking.package.id
        package_name = booking.package.title
        price = booking.package.price

        payment_date = datetime.now().date()

        booking.status = 'CONFIRMED'
        booking.save()

        payment_data = {
            "booking" : booking_id,
            "payment_date" : payment_date,
            "amount" : price
        }     

        request.data.update(payment_data)
        
        send_email.delay(user_email,user_name, booking_id, package_id, package_name, price)
        
        return super().create(request, *args, **kwargs)