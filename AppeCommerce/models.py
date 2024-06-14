from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

class Cart(models.Model):
    products = models.ManyToManyField(Product)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)