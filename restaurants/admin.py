from django.contrib import admin
from .models import RestaurantOwner, Restaurant, Menu

admin.site.register(RestaurantOwner)
admin.site.register(Restaurant)
admin.site.register(Menu)
