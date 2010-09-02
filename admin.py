from django.contrib import admin

from grocheris.models import GroceryItem, Location, LocationSection

admin.site.register(GroceryItem)
admin.site.register(Location)
admin.site.register(LocationSection)
