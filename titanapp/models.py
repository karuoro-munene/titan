from django.db import models
from django.utils import timezone


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phonenumber = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    zip = models.CharField(max_length=500, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.name


stati = (
    ("Item in US Warehouse", "Item in US Warehouse"),
    ("Item in Transit to Kenya", "Item in Transit to Kenya"),
    ("Item in Kenyan Warehouse", "Item in Kenyan Warehouse"),
    ("Item Sent for Delivery (Kenya)", "Item Sent for Delivery (Kenya)"),
)


class Package(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phonenumber = models.CharField(max_length=100, null=True, blank=True)
    invoice_number = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, choices=stati, default="Item in US Warehouse")
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.invoice_number
