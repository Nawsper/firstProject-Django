from django.urls import path
from . import views


app_name = "carrito"

urlpatterns = [
    path('carrito/', views.carrito, name='carrito'),
    path('agregar/<int:product_id>/', views.addProduct, name='agregar'),
    path('sumar/<int:product_id>/', views.plusProduct, name='sumar'),
    path('eliminar/<int:product_id>/', views.restProduct, name='eliminar'),
    path('quitar/<int:product_id>/', views.deleteProduct, name='quitar'),
    path('limpiar/', views.cleanCarrito, name='limpiar'),
]
