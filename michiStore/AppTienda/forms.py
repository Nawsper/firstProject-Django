from django import forms


class NuevoUsuario(forms.Form):
    Nombre = forms.CharField(max_length=30)
    Apellido = forms.CharField(max_length=30)
    Direccion = forms.CharField(max_length=50)
    Email = forms.EmailField()
    Telefono = forms.CharField(max_length=20)
