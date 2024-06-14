from django.urls import path
from titanapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("air-shipping",views.air, name="air"),
    path("sea-shipping",views.sea, name="sea"),
    path("you-buy-we-ship",views.youbuyweship, name="you-buy-we-ship"),
    path("cost-calculator",views.pricing, name="pricing"),
    path("what-people-ship",views.whatpeopleship, name="what-people-ship"),
    path("track-your-package",views.trackpackage, name="track-package"),
    path("ajax/process-book-pickup",views.processbook, name="book-pickup"),
]
