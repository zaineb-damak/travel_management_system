from package.models import Package, Day, Liked
from package.serializers import PackageSerializer,DaySerializer, LikedSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

class PackageList(generics.ListAPIView):
    serializer_class = PackageSerializer
    page_size = 10

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
    

class DayList(generics.ListAPIView):
    serializer_class = DaySerializer
    page_size = 10

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

class LikedList(generics.ListAPIView):
    serializer_class = LikedSerializer
    page_size = 10

    def get_queryset(self):
        user = self.request.user
        return Liked.objects.filter(user=user)


class LikedCreate(generics.CreateAPIView):
    serializer_class = LikedSerializer

    def create(self, request, *args, **kwargs):
        # Retrieve the package object
        try:
            package = Package.objects.get(pk=self.kwargs.get('pk'))
        except Package.DoesNotExist:
            return Response({"error": "Package does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        # Set the package ID in the request data
        request.data['package'] = package.id
        
        # Set the user ID in the request data
        request.data['user'] = request.user.id
        
        return super().create(request, *args, **kwargs)


