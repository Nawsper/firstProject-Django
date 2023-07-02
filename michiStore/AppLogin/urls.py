from django.urls import path
from .views import RegistroLogin, logOut, loguear


urlpatterns = [
    path('', RegistroLogin.as_view(), name='login'),
    path('logout', logOut, name='logout'),
    path('loguear', loguear, name='loguear'),
]
