from django.db import models

# Create your models here.

class LoanApplication(models.Model):

    name = models.CharField(max_length=12)
    income = models.IntegerField()
    mobile_no = models.BigIntegerField(blank=True,unique=True,error_messages ={
                    "unique":"The mobile number you entered is already register.Pls try again!"
                    })
    address = models.CharField(max_length=30,blank=True)




