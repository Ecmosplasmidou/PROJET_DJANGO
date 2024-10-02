from django.contrib import admin
from django.urls import path
from listing import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.base, name="base"),
    path("hello/", views.hello, name="hello"),
    path("about-us/", views.about, name="about"),
    path("listings/", views.listings, name="listings"),
    path("contact-us/", views.contact, name="contact"),
]
