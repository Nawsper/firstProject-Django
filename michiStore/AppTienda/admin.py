from django.contrib import admin
from .models import *

# Register your models here.


class ClientesAdmin(admin.ModelAdmin):
    list_display = ("name", "lastname", "email")
    search_fields = ("email",)


class ProductosAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "category")
    list_filter = ("category",)


class PedidosAdmin(admin.ModelAdmin):
    list_display = ("number", "date")
    list_filter = ("date",)
    date_hierarchy = "date"


admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Pedido, PedidosAdmin)
