from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Proyecto)
admin.site.register(Sistema)
admin.site.register(Usuario)
admin.site.register(ProyectoSistema)
admin.site.register(UsuarioProyectoSistema)