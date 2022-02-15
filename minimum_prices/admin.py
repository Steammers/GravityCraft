from django.contrib import admin
from minimum_prices.models import *

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Mod)
class ModAdmin(admin.ModelAdmin):
    pass
