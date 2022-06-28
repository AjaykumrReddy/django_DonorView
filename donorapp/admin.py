from django.contrib import admin
from .models import Donor, City

# Register your models here.


class DonrAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'gender',
        'Age',
        'Blood_Group',
        'phone',
        'city',
    )


admin.site.register(Donor, DonrAdmin)
admin.site.register(City)
