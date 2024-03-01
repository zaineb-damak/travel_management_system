from django.db import models
from booking.models import Booking
import hashlib

class Payment(models.Model):

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    credit_card = models.IntegerField(max_length=16)
    pin = models.CharField(max_length=128) 
    payment_date = models.DateField()
    amount = models.FloatField()

    def save(self, *args, **kwargs):
        if self.pin:
            hash_object = hashlib.sha256(str(self.pin).encode())
            self.pin = hash_object.hexdigest()
        
        super().save(*args, **kwargs)