from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^articulos/$', views.ListaArticulosView.as_view(), name='articulos'),
	url(r'^reservas/(?P<pk>\d+)$', views.ReservasView.as_view(), name='Reservas'),
]