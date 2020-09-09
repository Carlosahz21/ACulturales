from django.contrib import admin
from .models import Parroquia, Categoria, AmbitoCultural, Agrupacion


class ParroquiaAdmin(admin.ModelAdmin):
	search_fields = ("nombre_parroquia",
					 "nombre_presidente", 
					 "direccion_parroquia", 
					 "telefono_parroquia", 
					 "correo_parroquia")


admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Categoria)
admin.site.register(AmbitoCultural)
admin.site.register(Agrupacion)

