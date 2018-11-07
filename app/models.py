from django.db import models

# Create your models here.
class Reservation(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    fa_name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10,primary_key=True)
    email=models.EmailField()
    add=models.CharField(max_length=100)
    u_name=models.CharField(max_length=50)
    u_pass=models.IntegerField(default=10)
class payment(models.Model):
    name=models.CharField(max_length=50)
    c_no=models.IntegerField(default=10,primary_key=True)
    cvv=models.IntegerField(default=3)
    amount=models.IntegerField(default=10)
    des=models.CharField(max_length=100)
