from django.contrib import admin
from django.urls import path
from listing import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.base, name="base"),
    path("bands/", views.band_list, name="band_list"),
    path("bands/<int:band_id>/", views.band_detail, name="band_detail"),
    path("bands/<int:band_id>/edit/", views.band_edit, name="band_edit"),
    path('bands/<int:band_id>/delete/', views.band_delete, name='band_delete'),
    path("bands/add/", views.band_add, name="band_add"),
    path("listings/", views.listings, name="listings"),
    path('listings/add/', views.listings_add, name='listings_add'),
    path("listings/<int:id>/", views.listings_detail, name="listings_detail"),
    path("listings/<int:id>/edit/", views.listings_edit, name="listings_edit"),
    path('listings/<int:id>/delete/', views.listings_delete, name='listings_delete'),
    path("about-us/", views.about, name="about"),
    path("contact-us/", views.contact, name="contact"),
    path("email-sent/", views.email_sent, name="email-sent"),
]