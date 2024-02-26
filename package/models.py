from django.db import models
from django.conf import settings 

class Package(models.Model):
    title = models.CharField(max_length = 250)
    destination = models.CharField(max_length = 250)
    duration = models.TextField()
    price   = models.FloatField()
    def __str__(self):
        return self.destination

class Day(models.Model):
    title = models.CharField(max_length = 250)
    content = models.TextField()
    package = models.ForeignKey(Package, related_name='days', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Hotel(models.Model):
    title = models.CharField(max_length = 250)
    package = models.ForeignKey(Package, related_name='hotels', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Liked(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='liked', on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='liked', on_delete=models.CASCADE)