from django import forms
from django.forms import DateInput


class NuevoUsuario(forms.Form):
    Nombre = forms.CharField(max_length=30)
    Apellido = forms.CharField(max_length=30)
    Direccion = forms.CharField(max_length=50)
    Email = forms.EmailField()
    Telefono = forms.CharField(max_length=20)


class NuevoPedido(forms.Form):
    Numero = forms.IntegerField()
    Fecha = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    Enviado = forms.BooleanField()


class NuevoProducto(forms.Form):
    Titulo = forms.CharField(max_length=100)
    Precio = forms.IntegerField()
    Categoria = forms.CharField(max_length=15)
    Descripcion = forms.CharField(
        widget=forms.Textarea, initial='Descripción no disponible')
    Stock = forms.IntegerField()
