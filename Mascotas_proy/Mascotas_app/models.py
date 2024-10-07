from django.db import models

# Create your models here.

class Propietario(models.Model):
    nombre = models.CharField (verbose_name= 'Nombre Del Propietario ', max_length=100)
    apellido = models.CharField (verbose_name= 'Apellido Del Propietario ', max_length=100)
    ciudad = models.CharField (verbose_name= 'Ciudad Del Propiertario ', max_length=100)
    direccion = models.CharField (verbose_name= 'Direccion Del Propiertario ', max_length=100)
    telefono = models.CharField (verbose_name= 'Telefono Del Propiertario ', max_length=100)
    correo = models.CharField (verbose_name= 'Correo Del Propiertario ', max_length=100)
    contraseña = models.CharField (verbose_name= 'Contraseña Del Propiertario ', max_length=100)
    activo = models.BooleanField (verbose_name= 'Usuario Activo ', default=True)

    def __str__ (self):
        return self.nombre, self.apellido

class Mascota (models.Model):
    codigo = models.CharField (verbose_name= 'Codigo De La Mascota ', max_length=100)
    nombre = models.CharField (verbose_name= 'Nombre De La Mascota ', max_length=100)
    especie = models.CharField (verbose_name= 'Especie De La Mascota ', max_length=100)
    raza = models.CharField (verbose_name= 'Raza De La Mascota ', max_length=100)
    edad = models.DecimalField (verbose_name= 'Edad De La Mascota ', max_digits=10, decimal_places=2)
    peso = models.DecimalField (verbose_name= 'Peso De La Mascota ', max_digits=10, decimal_places=2)
    id_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='mascota')
    
    def __str__(self) :
        return self.nombre, self.especie