from django.contrib import admin
from .models import *

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    list_per_page = 10

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','designation']
    list_per_page = 15

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 20

@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ['name', 'checkout_time','return_time']
    ordering = ['checkout_time','return_time']
    list_per_page = 20


