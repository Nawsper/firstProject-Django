from django.urls import path
from AppTienda import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('busqueda/', views.busqueda_productos, name='busqueda'),
    path('buscar/', views.buscar)


]
