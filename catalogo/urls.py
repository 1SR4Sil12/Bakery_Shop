from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^articulos/$', views.ListaArticulosView.as_view(), name='articulos'),
	url(r'^clientes/$', views.ListaClientesView.as_view(), name='clientes'),
	url(r'^reservas/$', views.ListaReservasView.as_view(), name='reservas'),
]

#(?P<pk>\d+)