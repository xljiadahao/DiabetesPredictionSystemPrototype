from django.db import models

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=8, unique=True)
    description = models.CharField(max_length=22)
    price = models.IntegerField()
 
    def __str__(self):
        return self.description
 
    class Admin: pass
 
class Customer(models.Model):
    cid = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=25)
    products = models.ManyToManyField(Product)
 
    def __str__(self):
        return self.name
 
    class Admin: pass
