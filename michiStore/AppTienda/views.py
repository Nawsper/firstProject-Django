from django.shortcuts import render, redirect
from AppTienda.models import Producto
from .forms import FormContacto


def inicio(request):
    return render(request, "index.html")


def nosotros(request):
    return render(request, "nosotros.html")


def productos(request):
    productos = Producto.objects.all()
    return render(request, "productos.html", {"productos": productos})


def contacto(request):
    if request.method == 'POST':
        form = FormContacto(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            lastname = request.POST.get("lastname")
            email = request.POST.get("email")
            content = request.POST.get("content")
            message = request.POST.get("message")
            accept = request.POST.get("accept")
            return redirect("/contacto/?enviado")
    else:
        form = FormContacto()

    return render(request, 'contacto.html', {'form': form})
