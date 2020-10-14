from django.contrib import admin

# Register your models here.

from .models import Cliente, Categoria, Articulo, Reserva

# admin.site.register(Cliente)
admin.site.register(Categoria)
# admin.site.register(Articulo)
# admin.site.register(Reserva)

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellidos', 'telefono')
	fields = ['nombre', 'apellidos', ('telefono')]

admin.site.register(Cliente, ClienteAdmin)

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'precio')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
	list_display = ('id', 'cliente', 'articulo', 'cantidad', 'fecha_reserva')
	list_filter = ('estado', 'fecha_reserva')

	fieldsets = (

		('Compra', {
			'fields': ('articulo', 'cantidad')
		}),
		('Disponibilidad', {
			'fields': ('estado', 'fecha_reserva')
		}),

	)