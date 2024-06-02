from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
class Weapon(models.Model):
    power = models.IntegerField()
    rarity = models.CharField(max_length=50)
    value = models.IntegerField()
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = (models.IntegerField())
    category = models.CharField(max_length=50)
    units = models.CharField(max_length=5)
    def __str__(self):
        return f'{self.name}, {self.units}, {self.price}'


class Order(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    sum = models.IntegerField()
    pass
    # products = models.ManyToManyField(Product, related_name='orders')

class OrderPosition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='positions')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions')
    quantity = models.IntegerField()
    sum = models.IntegerField()
class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.brand}, {self.model}, {self.color}'

class Person(models.Model):
    name = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='owners')