from django.urls import path
from .views import inicio, nosotros, productos, contacto  # , notFound

urlpatterns = [
    path('', inicio),
    path('nosotros/', nosotros),
    path('productos/', productos),
    path('contacto/', contacto),
    # path('*', notFound)

]
