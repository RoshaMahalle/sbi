from django.contrib import admin
from .models import SavingApplication

# Register your models here.

class SaveAdmit(admin.ModelAdmin):
    list_display = ['name','accountno','ifsccode','branch','address','pincode']

admin.site.register(SavingApplication, SaveAdmit)
