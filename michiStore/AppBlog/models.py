from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Categorias(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class meta:
        vebose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name


class Entradas(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=6000)
    img = models.ImageField(upload_to="AppTienda", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Categorias)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
