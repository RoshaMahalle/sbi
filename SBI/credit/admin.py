from django.contrib import admin
from .models import CreditApplication

# Register your models here.

class CreditApplicationAdmin(admin.ModelAdmin):

    list_display = ['name','email','password']

admin.site.register(CreditApplication,CreditApplicationAdmin)