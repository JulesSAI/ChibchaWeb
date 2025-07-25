from django.contrib import admin
from .models import Cliente, Direccion, Tarjeta
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Direccion)
admin.site.register(Tarjeta)