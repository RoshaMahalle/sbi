from django.contrib import admin
from .models import DepositApplication

# Register your models here.

class DepositApplicationAdmin(admin.ModelAdmin):

    list_display = ['name','depoMoney','email']

admin.site.register(DepositApplication, DepositApplicationAdmin)
