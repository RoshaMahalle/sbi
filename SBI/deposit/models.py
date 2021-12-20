from django.db import models

# Create your models here.
class DepositApplication(models.Model):

    name = models.CharField(max_length=20)
    depoMoney = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=30, blank=True)

