from django import forms
from .models import Donation, Crisis 

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount']
        

class CrisisForm(forms.ModelForm):
    class Meta:
        model = Crisis
        fields = ['title', 'location', 'description', 'status', 'severity', 'required_help']