from django.contrib import admin
from .models import Package, Day, Hotel, Liked

admin.site.register(Package)
admin.site.register(Day)
admin.site.register(Hotel)
admin.site.register(Liked)
