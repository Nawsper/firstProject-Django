from django.shortcuts import render, redirect
from .carrito import Carrito
from AppTienda.models import Producto


# Create your views here.

def carrito(request):
    return render(request, "carrito/carrito.html")


def addProduct(request, product_id):
    carrito = Carrito(request)
    product = Producto.objects.get(id=product_id)
    carrito.addCarrito(product)
    return redirect("productos")


def plusProduct(request, product_id):
    carrito = Carrito(request)
    product = Producto.objects.get(id=product_id)
    carrito.plusCarrito(product)
    return render(request, "carrito/carrito.html")


def deleteProduct(request, product_id):
    carrito = Carrito(request)
    product = Producto.objects.get(id=product_id)
    carrito.deleteProd(product=product)
    return render(request, "carrito/carrito.html")


def restProduct(request, product_id):
    carrito = Carrito(request)
    product = Producto.objects.get(id=product_id)
    carrito.restProd(product=product)
    return render(request, "carrito/carrito.html")


def cleanCarrito(request):
    carrito = Carrito(request)
    carrito.cleanCarrito()
    return render(request, "carrito/carrito.html")


def envio(request):
    return render(request, "carrito/finalCompra.html")
