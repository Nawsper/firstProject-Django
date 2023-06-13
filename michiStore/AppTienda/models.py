from django.db import models

# Create your models here.


class Cliente(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Producto(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.title


class Pedido(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    sent = models.BooleanField()
