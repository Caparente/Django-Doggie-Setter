from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pet_name', 'pet_type', 'service', 'date', 'owner_name', 'email', 'phone_number']
        

