from django import forms
from .models import SavingApplication

class SavingApplicationForm(forms.ModelForm):
    class Meta:
        model = SavingApplication
        fields ="__all__"
