from django.db import models

class Pregunta(models.Model):
	texto = models.CharField(max_length=200)
	fecha_pub = models.DateTimeField('date published')

	def __str__(self):
		return self.texto

class Opcion(models.Model):
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	texto = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)

	def __str__(self):
		return self.texto