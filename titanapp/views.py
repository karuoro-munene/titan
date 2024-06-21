import json

from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Booking, Package


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


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def bookings(request):
    bookings = Booking.objects.all()
    return render(request, "bookings.html", locals())


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def booking(request, id):
    booking = Booking.objects.get(id=id)
    booking.read = True;
    booking.save()
    return render(request, "booking.html", locals())


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def package(request, id):
    package = Package.objects.get(id=id)
    return render(request, "package.html", locals())


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def managepackages(request):
    packages = Package.objects.all()
    return render(request, "manage-packages.html", locals())


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def administration(request):
    return render(request, "administration.html", locals())


def processbook(request):
    dict = request.POST.dict()
    if request.method == 'POST':
        try:
            booking = Booking.objects.create(name=dict['name'],
                                             address=f"{dict['address']}, {dict['city']},{dict['state']}, {dict['zip']}",
                                             city=dict['city'],
                                             state=dict['state'],
                                             zip=dict['zip'],
                                             phonenumber=dict['phonenumber'], message=dict['message'])
            booking.save()
            message = {"message": "Booking successfully created"}
        except Exception as e:
            message = {"message": str(e)}

    return HttpResponse(json.dumps(message), content_type='application/json')


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def addpackage(request):
    dict = request.POST.dict()
    if request.method == 'POST':
        try:
            package = Package.objects.create(name=dict['name'],
                                             phonenumber=dict['phonenumber'],
                                             invoice_number=dict['invoice'],
                                             status=dict['status'])
            package.save()
            message = {"message": "Package successfully saved"}
        except Exception as e:
            message = {"message": str(e)}
    # TWILIO: 5JWQ9NEYZNB7W9MX7G7DLP37

    return HttpResponse(json.dumps(message), content_type='application/json')


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def editpackage(request):
    dict = request.POST.dict()
    if request.method == 'POST':
        try:
            package = Package.objects.get(id=int(dict['id']))
            package.name = dict['name']
            package.invoice_number = dict['invoice']
            package.status = dict['status']
            package.phonenumber = dict['phonenumber']
            package.save()
            message = {"message": "Package successfully edited"}
        except Exception as e:
            message = {"message": str(e)}
    # TWILIO: 5JWQ9NEYZNB7W9MX7G7DLP37

    return HttpResponse(json.dumps(message), content_type='application/json')
