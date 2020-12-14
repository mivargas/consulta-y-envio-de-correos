from django.db import models

# Create your models here.

class Clientes(models.Model):
	nombre=models.CharField(max_length=30)
	direccion=models.CharField(max_length=50, verbose_name="Domicilio") #se crea un alias para mostrar en vez del nombre de la tabla en el panel de admin
	email=models.EmailField(blank=True, null=True) #esto es para que sea opcional en el panel de administraion
	tfno=models.CharField(max_length=7)

	def __str__(self):
		return self.nombre

class Articulos(models.Model):
	nombre=models.CharField(max_length=30)
	seccion=models.CharField(max_length=20)
	precio=models.IntegerField()

	def __str__(self):
		return 'el nombre es %s la seccion es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
	numero=models.IntegerField()
	fecha=models.DateField()
	entregado=models.BooleanField()
