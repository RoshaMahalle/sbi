from django.db import models

# Create your models here.

class CreditApplication(models.Model):

    name = models.CharField(max_length=50)
    credit =models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20 )

