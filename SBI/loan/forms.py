from django import forms
from .models import LoanApplication
from django.contrib.auth.models import User

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields ="__all__"

    def clean_income(self):
       inputincome = self.cleaned_data['income']
       if inputincome<25000:
           raise forms.ValidationError(("Salary must be more than 25k"), code='invalid')
       return inputincome

    def clean(self):
        super(LoanApplicationForm, self).clean()
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            self._errors['name'] = self.error_class([
                'Minimum 3 characters required'])
        return self.cleaned_data

    def clean_mobile_no(self):
        mobile_no = self.cleaned_data['mobile_no']
        return mobile_no


class SignupForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields = ['username','password','email','first_name','last_name']