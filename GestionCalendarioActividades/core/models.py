from django.db import models
# Create your models here.

TIPO_CHOICES = [
    ("V", "Vacaciones"),
    ("F", "Feriado"),
    ("SA", "Suspencion de Actividades"),
    ("SAP", "Suspencion de Actividades PM"),
    ("P", "Periodo Lectivo"),
    ("SE", "Suspension de Evaluaciones"),
    ("C", "Ceremonia"),
    ("ED", "EDDA"),
    ("E", "Evaluacion"),
    ("A", "Ayudantias"),
    ("H", "Hito Academico"),
    ("S", "Secretaria Academica"),
    ("O", "OAI")]

class Segmento(models.Model):
    C = "Comunidad USM",
    E = "Estudiante",
    P = "Profesor",
    J= "Jefe de Carrerra"
    def __str__(self) -> str:
        return self.titulo

class Evento(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    titulo = models.CharField(max_length=75)
    descripcion = models.CharField(max_length=700)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default = 'S')
    segmento = models.ManyToManyField(Segmento)
    def __str__(self) -> str:
        return self.titulo
    