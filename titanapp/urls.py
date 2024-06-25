from django.urls import path
from titanapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("air-shipping", views.air, name="air"),
    path("sea-shipping", views.sea, name="sea"),
    path("you-buy-we-ship", views.youbuyweship, name="you-buy-we-ship"),
    path("cost-calculator", views.pricing, name="pricing"),
    path("what-people-ship", views.whatpeopleship, name="what-people-ship"),
    path("track-your-package", views.trackpackage, name="track-package"),
    path("maureen", views.maureen, name="maureen"),
    path("ajax/process-book-pickup", views.processbook, name="book-pickup"),
    path("ajax/add-package", views.addpackage, name="add-package"),
    path("ajax/edit-package", views.editpackage, name="edit-package"),
    path("administration", views.administration, name="administration"),
    path("administration/manage-packages", views.managepackages, name="manage-packages"),
    path("administration/package/id/<int:id>", views.package, name="package"),
    path("administration/bookings", views.bookings, name="manage-bookings"),
    path("administration/booking/id/<int:id>", views.booking, name="booking"),
    path("administration/update-tracking", views.updatetracking, name="updatetracking"),
]
