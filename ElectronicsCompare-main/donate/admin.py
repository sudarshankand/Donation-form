from django.contrib import admin
from .models import PersonDonation

# Register your models here.

class PersonDonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address', 'email', 'what_to_donate', 'date')

# Register your models here.
admin.site.register(PersonDonation, PersonDonationAdmin)