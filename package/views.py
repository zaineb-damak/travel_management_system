from package.models import Package, Day, Liked, Hotel
from package.serializers import PackageSerializer,DaySerializer, LikedSerializer, HotelSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

class PackageList(generics.ListAPIView):
    serializer_class = PackageSerializer
    page_size = 10
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Package.objects.all()
        destination = self.request.query_params.get('destination')
        if destination is not None:
            queryset = queryset.filter(destination=destination)
        return queryset

class PackageDetail(generics.RetrieveAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    page_size = 10
    permission_classes = [AllowAny]

class DayList(generics.ListAPIView):
    serializer_class = DaySerializer
    page_size = 10
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Day.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset

class DayDetail(generics.RetrieveAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    page_size = 10
    permission_classes = [AllowAny]

class HotelList(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    page_size = 10
    permission_classes = [AllowAny]

class HotelDetail(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    page_size = 10
    permission_classes = [AllowAny]

class LikedList(generics.ListAPIView):
    serializer_class = LikedSerializer
    page_size = 10
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Liked.objects.all().filter(user=self.request.user)
        return queryset


class LikedCreate(generics.CreateAPIView):
    serializer_class = LikedSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        # Retrieve the package object
        try:
            package = Package.objects.get(pk=self.kwargs.get('pk'))
        except Package.DoesNotExist:
            return Response({"error": "Package does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        request.data['package'] = package.id
        
        request.data['user'] = request.user.id
        
        return super().create(request, *args, **kwargs)


