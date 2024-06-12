from django.contrib import admin
from .models import Marca , Producto
# Register your models here.


#registramos las tablas en admin para que aparescan en la web admin para gestionar crud
admin.site.register(Marca)
admin.site.register(Producto)
