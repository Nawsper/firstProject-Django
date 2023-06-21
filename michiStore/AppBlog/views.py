from django.shortcuts import render
from AppBlog.models import Entradas

# Create your views here.


def blog(request):
    entradas = Entradas.objects.all()
    return render(request, "blog/blog.html", {"entradas": entradas})
