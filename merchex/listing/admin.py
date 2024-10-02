from django.contrib import admin
from .models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed', 'active')
admin.site.register(Band, BandAdmin)

class ListinAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'year', 'band', 'sold')
admin.site.register(Listing, ListinAdmin)