from django.contrib import admin
from .models import Customers, Measurement


class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('customer', 'title', 'len', 'waist', 'amount')


admin.site.register(Measurement, MeasurementAdmin)


class CustomersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'mobile_no', 'address')


admin.site.register(Customers, CustomersAdmin)
