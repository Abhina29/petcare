from django.db import models

# Create your models here.
class contactdb(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=20,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    message=models.CharField(max_length=20,null=True,blank=True)
class appoinmentdb(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=20,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    purpose=models.CharField(max_length=20,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
class registerdb(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=20,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)
class requestdb(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    breed=models.CharField(max_length=50,null=True,blank=True)