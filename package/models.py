from django.db import models

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