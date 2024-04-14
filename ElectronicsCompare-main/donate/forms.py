from django import forms
from .models import PersonDonation

class PersonDonationForm(forms.ModelForm):
    class Meta:
        model = PersonDonation
        fields = ['name', 'phone_number', 'address', 'email', 'what_to_donate', 'date']
