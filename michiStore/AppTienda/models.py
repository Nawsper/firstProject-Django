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


class Pedido(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    sent = models.BooleanField()


class CategoriaProd(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoryProd"
        verbose_name_plural = "categoriesProd"

    def __str__(self):
        return self.name


class Producto(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey('CategoriaProd', on_delete=models.CASCADE)
    description = models.TextField(default='Descripción no disponible')
    stock = models.IntegerField(default=0)
    img = models.ImageField(upload_to='productos',
                            default='AppTienda/assets/img/default.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
