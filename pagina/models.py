from django.db import models

class Dificultad(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Prioridad(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=60)
    prioridad = models.ForeignKey(Prioridad)
    dificultad = models.ForeignKey(Dificultad)
    fecha_creacion =  models.DateField(auto_now_add = True)
    fecha_fin = models.DateField()
    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length = 60)
    actividades = models.ManyToManyField(Actividad)
    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=120)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    def __str__(self):
        return self.nombre

class Asignacion(models.Model):
    nombre_asignacion = models.CharField(max_length=60)
    empresa = models.ForeignKey(Empresa)
    proyectos = models.ManyToManyField(Proyecto)
    fondos = models.CharField(max_length=50)
    recursos_humano = models.IntegerField()
    def __str__(self):
        return self.nombre_asignacion
