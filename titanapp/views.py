import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import Booking


def home(request):
    return render(request, "index.html")


def air(request):
    return render(request, "air.html")


def sea(request):
    return render(request, "sea.html")


def youbuyweship(request):
    return render(request, "buy-ship.html")


def pricing(request):
    return render(request, "pricing.html")


def whatpeopleship(request):
    return render(request, "what-people-ship.html")


def trackpackage(request):
    return render(request, "track-package.html")

def bookings(request):
    return render(request, "bookings.html")


def processbook(request):
    dict = request.POST.dict()
    if request.method == 'POST':
        try:
            booking = Booking.objects.create(name=dict['name'],
                                             address=f"{dict['address']}, {dict['city']},{dict['state']}, {dict['zip']}",
                                             phonenumber=dict['phonenumber'], message=dict['message'])
            booking.save()
            message = {"message": "Booking successfully created"}
        except Exception as e:
            message = {"message": str(e)}

    return HttpResponse(json.dumps(message), content_type='application/json')
