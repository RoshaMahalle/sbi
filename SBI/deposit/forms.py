from django import forms

from .models import DepositApplication

class DeposteApplicationForm(forms.ModelForm):
    class Meta:
        model = DepositApplication
        fields = "__all__"

    def clean_depoMoney(self):
        inputdepoMoney = self.cleaned_data['depoMoney']
        if inputdepoMoney < 25000:
            raise forms.ValidationError(("Salary must be more than 25k"), code='invalid')
        return inputdepoMoney






