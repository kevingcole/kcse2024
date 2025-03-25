# it_asset/admin.py

from django.contrib import admin
from .models import ITAsset, Manufacturer, Employee

@admin.register(ITAsset)
class ITAssetAdmin(admin.ModelAdmin):
    list_display = ['name', 'serial_number', 'manufacturer', 'assigned_to']
    search_fields = ['name', 'serial_number']
    list_filter = ['manufacturer', 'assigned_to']

admin.site.register(Manufacturer)
admin.site.register(Employee)

""" # Register CustomUser only once
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # You can customize the admin interface for CustomUser here, for example:
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['username', 'email']

# Register CustomUser with its custom admin
admin.site.register(CustomUser, CustomUserAdmin) """