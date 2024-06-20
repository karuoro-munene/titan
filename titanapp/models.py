from django.db import models
from django.utils import timezone


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phonenumber = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.name
