import json

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render


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


def processbook(request):
    dict = request.POST.dict()
    # send_mail(
    #     "Someone just booked a pick up",
    #     f"Name: {dict['name']}, Address: {dict['address']}, {dict['city']}, {dict['state']}, {dict['zip']}, Phonenumber: {dict['']}, Message: {dict['message']}",
    #     "from@example.com",
    #     ["to@example.com"],
    #     fail_silently=
    # False,
    # )
    return HttpResponse(json.dumps(dict), content_type='application/json')
