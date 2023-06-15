from django.http import HttpResponse
from django.shortcuts import render
from AppTienda.models import Producto


def inicio(request):
    return render(request, "index.html")


def nosotros(request):
    return render(request, "nosotros.html")


def productos(request):
    return render(request, "productos.html")


def contacto(request):
    return render(request, "contacto.html")


def busqueda_productos(request):
    return render(request, "busquedaProd.html")


def buscar(request):
    if request.GET["prod"]:
        producto = request.GET["prod"]
        articulos = Producto.objects.filter(title__icontains=producto)
        return render(request, "detalleProducto.html", {"articulos": articulos, "query": producto})
    else:
        msj = "Introduce un campo valido"
    return HttpResponse(msj)
