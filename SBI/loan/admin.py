from django.contrib import admin
from .models import LoanApplication

# Register your models here.

class LoanAdmit(admin.ModelAdmin):
    list_display = ['name','income','mobile_no','address']

admin.site.register(LoanApplication, LoanAdmit)


