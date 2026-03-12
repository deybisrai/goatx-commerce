from django.contrib import admin

# Register your models here.

from .models import Categoria,Producto

admin.site.register(Categoria)

@admin.register(Producto)
class productoAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','categoria')
    list_editable = ()
    
