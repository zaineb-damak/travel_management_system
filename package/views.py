from package.models import Package, Day
from package.serializers import PackageSerializer,DaySerializer
from rest_framework import generics

class PackageList(generics.ListAPIView):
    queryset  = Package.objects.all()
    serializer_class = PackageSerializer
    page_size = 10

class PackageDetail(generics.RetrieveAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    page_size = 10

class DayList(generics.ListAPIView):
    queryset  = Day.objects.all()
    serializer_class = DaySerializer
    page_size = 10

class DayDetail(generics.RetrieveAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    page_size = 10



