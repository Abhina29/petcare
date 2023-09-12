from django.db import models

# Create your models here.
class petsdb(models.Model):
    pets=models.CharField(max_length=20,null=True,blank=True)
    breed=models.CharField(max_length=20,null=True,blank=True)
    image=models.ImageField(upload_to='profile',null=True,blank=True)
    rate=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=40000,null=True,blank=True)

class categorydb(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    image=models.ImageField(upload_to='profile',null=True,blank=True)
    description=models.CharField(max_length=30,null=True,blank=True)
class servicedb(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    image=models.ImageField(upload_to='profile',null=True,blank=True)
    description=models.CharField(max_length=1000,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
class acceptdb(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    breed = models.CharField(max_length=50, null=True, blank=True)