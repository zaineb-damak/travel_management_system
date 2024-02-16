from package.models import Package, Day
from package.serializers import PackageSerializer,DaySerializer
from rest_framework import generics

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






