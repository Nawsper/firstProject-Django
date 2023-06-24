from django.shortcuts import render
from AppBlog.models import Entradas, Categorias

# Create your views here.


def blog(request):
    entradas = Entradas.objects.all()
    categorias_set = set()
    for entrada in entradas:
        for categoria in entrada.category.all():
            categorias_set.add(categoria)
    return render(request, "blog/blog.html", {"entradas": entradas, "categorias_set": categorias_set})


def categoria(request, categoria_id):
    categoria = Categorias.objects.get(id=categoria_id)
    entradas = Entradas.objects.filter(category=categoria)
    return render(request, "blog/categorias.html", {'categoria': categoria, 'entradas': entradas})
