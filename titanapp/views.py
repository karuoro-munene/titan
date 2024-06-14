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
