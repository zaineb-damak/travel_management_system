from booking.models import Booking
from package.models import Package
from booking.serializers import BookingSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from booking.tasks import create_pdf_invoice_task

class BookingList(generics.ListAPIView):
    serializer_class = BookingSerializer
    page_size = 10

    def get_queryset(self):
        queryset = Booking.objects.all()
        title = self.request.query_params.get('package')
        if title is not None:
            queryset = queryset.filter(trip_package=title)
        return queryset

class BookingDetail(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    page_size = 10

class BookingCreate(generics.CreateAPIView):
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        # Retrieve the package object
        try:
            package = Package.objects.get(pk=self.kwargs.get('pk'))
        except Booking.DoesNotExist:
            return Response({"error": "Booking does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        request.data['status'] = 'PENDING'
        request.data['booking_date'] = datetime.now().date()
        request.data['package'] = package.id
        request.data['user'] = request.user.id
          
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        try:
            package = Package.objects.get(pk=self.kwargs.get('pk'))
        except Booking.DoesNotExist:
            return Response({"error": "Booking does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer.save(
            status='PENDING',
            booking_date=datetime.now().date(),
            package=package,
            user=self.request.user
        )

        # Call method to create PDF invoice
        booking_id = serializer.instance.id
        package_id = package.id
        user_id = self.request.user.id
        booking_date = datetime.now().date()

        create_pdf_invoice_task.delay(booking_id, booking_date, package_id, user_id)

        return super().perform_create(serializer)

class BookingDestroy(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer



