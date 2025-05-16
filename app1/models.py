from django.db import models


class ATM(models.Model):
    name=models.CharField(max_length=26)
    acc=models.CharField(max_length=12)
    ifsc=models.CharField(max_length=6)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=8)
    balance=models.DecimalField(max_digits=14,decimal_places=2)
