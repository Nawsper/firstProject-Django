from django import forms


class FormContacto(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100, required=True)
    lastname = forms.CharField(label='Apellido', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    content = forms.ChoiceField(label='Asunto', choices=[
        ('alimentos', 'Alimentos'),
        ('accesorios', 'Accesorios'),
        ('cuchas', 'Cuchas'),
        ('juguetes', 'Juguetes'),
        ('otros', 'Otros')
    ])
    message = forms.CharField(
        label='Dejanos un mensaje:', widget=forms.Textarea)
    accept = forms.BooleanField(
        label='Recibir email con novedades', required=False)
