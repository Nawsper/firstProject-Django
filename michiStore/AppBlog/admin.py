from django.contrib import admin
from .models import Categorias, Entradas

# Register your models here.


class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class EntradasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Entradas, EntradasAdmin)
