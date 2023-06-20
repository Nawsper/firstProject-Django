from django.http import HttpResponse
from django.shortcuts import render
from AppTienda.models import Producto, Cliente, Pedido
from AppTienda.forms import NuevoUsuario, NuevoPedido, NuevoProducto


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
        if len(producto) > 20:
            msj = "Maximo 20 caracteres"
        else:
            articulos = Producto.objects.filter(title__icontains=producto)
            return render(request, "detalleProducto.html", {"articulos": articulos, "query": producto})
    else:
        msj = "Introduce un campo valido"
    return HttpResponse(msj)


def contacto(request):
    if request.method == "POST":
        return render(request, "formEnviado.html")
    return render(request, "contacto.html")


def nuevoUsuario(request):
    if request.method == 'POST':
        newUser = NuevoUsuario(request.POST)
        if newUser.is_valid():
            infoUsuario = newUser.cleaned_data
            usuario = Cliente(
                name=infoUsuario['Nombre'], lastname=infoUsuario['Apellido'], address=infoUsuario['Direccion'], email=infoUsuario['Email'], phone=infoUsuario['Telefono'])
            usuario.save()
            return render(request, "formEnviado.html")
    else:
        newUser = NuevoUsuario()
    return render(request, "registro.html", {"newUser": newUser})


def nuevoPedido(request):
    if request.method == 'POST':
        nuevoPedidoForm = NuevoPedido(request.POST)
        if nuevoPedidoForm.is_valid():
            infoPedido = nuevoPedidoForm.cleaned_data
            pedido = Pedido(
                number=infoPedido['Numero'], date=infoPedido['Fecha'], sent=infoPedido['Enviado'])
            pedido.save()
            return render(request, "formEnviado.html")
    else:
        nuevoPedidoForm = NuevoPedido()
    return render(request, "registroPedido.html", {"nuevoPedidoForm": nuevoPedidoForm})


def nuevoProducto(request):
    if request.method == 'POST':
        nuevoProductoForm = NuevoProducto(request.POST)
        if nuevoProductoForm.is_valid():
            infoProducto = nuevoProductoForm.cleaned_data
            producto = Producto(
                title=infoProducto['Titulo'], price=infoProducto['Precio'],
                category=infoProducto['Categoria'], description=infoProducto['Descripcion'],
                stock=infoProducto['Stock'])
            producto.save()
            return render(request, "formEnviado.html")
    else:
        nuevoProductoForm = NuevoProducto()
    return render(request, "registroProducto.html", {"nuevoProductoForm": nuevoProductoForm})
