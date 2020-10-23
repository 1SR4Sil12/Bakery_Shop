from django.db import models

# Create your models here.

class Categoria(models.Model):
	tipo = models.CharField(max_length=15, help_text="Ingresa la categoría.")

	def __str__(self):
		return self.tipo

class Articulo(models.Model):
	nombre = models.CharField(max_length=100)
	precio = models.FloatField(default=0)
	tipo = models.ManyToManyField(Categoria, help_text="Selecciona una categoria.")

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return self.nombre

class Cliente(models.Model):
	nombre = models.CharField(max_length=30, help_text="Ingresa tu nombre.")
	apellidos = models.CharField(max_length=50, help_text="Ingresa tus apellidos.")
	telefono = models.IntegerField(help_text="Ingresa tu número de teléfono.")

	def __str__(self):
		return '%s %s, %s' % (self.nombre, self.apellidos, self.telefono)

import uuid

class Reserva(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para esta reserva.")
	fecha_reserva = models.DateField(null=True, blank=True)
	cantidad = models.IntegerField(default=0, help_text="Ingresa la cantidad que quieres.")
	articulo = models.ForeignKey(Articulo, on_delete=models.SET_NULL, null=True)
	cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)

	LOAN_STATUS = (
		('e', 'Entregado'),
		('p', 'Pendiente'),
		('c', 'Cancelada'),
		('n', 'No disponible')
	)

	estado = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='p', help_text='Estado del pedido.')

	class Meta:
		ordering = ["fecha_reserva"]

	def __str__(self):
		return '%s (%s, %s %s, %s)' % (self.id, self.articulo.nombre, self.cliente.nombre, self.cliente.apellidos, self.fecha_reserva)