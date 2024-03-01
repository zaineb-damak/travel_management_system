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
        try:
            package = Package.objects.get(pk=self.kwargs.get('pk'))
        except Booking.DoesNotExist:
            return Response({"error": "Booking does not exist"}, status=status.HTTP_404_NOT_FOUND)
       
       
        package_data = {
            "id": package.id,  
            "destination": package.destination,
            "duration": package.duration,
            "price": package.price  
         }
        request.data['status'] = 'PENDING'
        request.data['booking_date'] = datetime.now().date()
        request.data['package'] = package_data
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

        
        booking_id = serializer.instance.id
        package_id = package.id
        user_id = self.request.user.id
        booking_date = datetime.now().date()
        price = package.price
        destination = package.destination

        create_pdf_invoice_task.delay(booking_id, booking_date, package_id, user_id, price, destination)

        return super().perform_create(serializer)

class BookingDestroy(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingCancel(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_update(self, serializer):
        serializer.instance.status = 'CANCELLED'
        serializer.instance.save()


