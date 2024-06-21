from django.urls import path, include

urlpatterns = [
    path("", include("titanapp.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
