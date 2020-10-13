from django.db import models

# Create your models here.

class Categoria(models.Model):
	tipo = models.CharField(max_length=15, help_text="Ingresa la categoría.")

	def __str__(self):
		return self.tipo

class Articulo(models.Model):
	nombre = models.CharField(max_length=100)
	precio = models.IntegerField(default=0)
	tipo = models.ForeingKey(Categoria, on_delete=models.SET_NULL, null=True, help_text="Selecciona una categoria.")

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('articulo-detail', args=[str(self.id)])

class Reserva(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para esta reserva")
	fecha = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
		('e', 'Entregado'),
		('p', 'Pendiente'),
		('c', 'Cancelada'),
	)

	estado = 