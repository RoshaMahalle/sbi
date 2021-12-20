from django.db import models

# Create your models here.
class SavingApplication(models.Model):

    name = models.CharField(max_length=25)
    accountno =  models.IntegerField()
    ifsccode = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    pincode = models.IntegerField()
