from django.urls import path
from AppTienda import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('busqueda/', views.busqueda_productos, name='busqueda'),
    path('buscar/', views.buscar),
    path('registro/', views.nuevoUsuario, name='registro'),
    path('registro_pedido/', views.nuevoPedido, name='registro_pedido'),
    path('registro_producto/', views.nuevoProducto, name='registro_producto'),
]
