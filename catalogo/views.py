from django.shortcuts import render

# Create your views here.

from .models import Cliente, Categoria, Articulo, Reserva

def index(request):
    num_articulos=Articulo.objects.all().count()
    num_reservas=Reserva.objects.all().count()
    num_reservas_disponibles=Reserva.objects.filter(estado__exact='p').count()
    num_clientes=Cliente.objects.count()
    
    return render(
        request,
        'index.html',
        context={'num_articulos':num_articulos,'num_reservas':num_reservas,'num_reservas_disponibles':num_reservas_disponibles,'num_clientes':num_clientes},
    )

from django.views import generic

class ListaArticulosView(generic.ListView):
	model = Articulo
	template = "templates/catalogo/articulo_list.html"
	context_object_name = "articulos_list"

class ListaClientesView(generic.ListView):
	model = Cliente
	template = "templates/catalogo/cliente_list.html"
    #context_object_name = "clientes_list"

class ListaReservasView(generic.ListView):
    model = Reserva
    template = "templates/catalogo/reserva_list.html"