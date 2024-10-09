from django.db import models
from datetime import *
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

# class Propietario(models.Model):
#     nombre = models.CharField (verbose_name= 'Nombre Del Propietario ', max_length=100)
#     apellido = models.CharField (verbose_name= 'Apellido Del Propietario ', max_length=100)
#     ciudad = models.CharField (verbose_name= 'Ciudad Del Propiertario ', max_length=100)
#     direccion = models.CharField (verbose_name= 'Direccion Del Propiertario ', max_length=100)
#     telefono = models.CharField (verbose_name= 'Telefono Del Propiertario ', max_length=100)
#     correo = models.CharField (verbose_name= 'Correo Del Propiertario ', max_length=100)
#     contraseña = models.CharField (verbose_name= 'Contraseña Del Propiertario ', max_length=100)
#     activo = models.BooleanField (verbose_name= 'Usuario Activo ', default=True)

#     def __str__ (self):
#         return self.nombre, self.apellido

# class Mascota (models.Model):
#     codigo = models.CharField (verbose_name= 'Codigo De La Mascota ', max_length=100)
#     nombre = models.CharField (verbose_name= 'Nombre De La Mascota ', max_length=100)
#     especie = models.CharField (verbose_name= 'Especie De La Mascota ', max_length=100)
#     raza = models.CharField (verbose_name= 'Raza De La Mascota ', max_length=100)
#     edad = models.DecimalField (verbose_name= 'Edad De La Mascota ', max_digits=10, decimal_places=2)
#     peso = models.DecimalField (verbose_name= 'Peso De La Mascota ', max_digits=10, decimal_places=2)
#     id_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='mascota')
    
#     def __str__(self) :
#         return self.nombre, self.especie

#MIERCOLES 09/10/2024
    
# class Producto (models.Model): 
#     codigo= models.CharField (verbose_name='Codigo Unico Del Producto',max_length=100,unique=True,null=False)
#     nombre= models.CharField (verbose_name='Nombre Del Producto',max_length=100,null=False)
#     descripcion= models.CharField (verbose_name='Descripción De Su Producto',max_length=255,null=False)
#     presentacion= models.CharField (verbose_name='Presentacion Del Producto',max_length=100,null=False)
#     pais_origen= models.CharField (verbose_name='Pais De Donde Viene El Producto',max_length=100,null=False)
#     activo= models.BooleanField (verbose_name= 'Producto Activo ', default=True,null=False)
#     fecha_fabric= models.DateField (verbose_name='Fecha De Fabricación',default=date.today,null=False)
#     fecha_vencido=models.DateField (verbose_name='Fecha Vencimiento ',default=date.today,null=True)
#     precio= models.DecimalField (max_digits=10, decimal_places=2)
#     stock= models.IntegerField (default=0,validators=[MinValueValidator(0),MaxValueValidator(1000)],help_text='Cantidad De Productos En El Inventario',null=False)
    

class Persona (models.Model):
    codigo= models.CharField(verbose_name='Codigo Unico de Reconocimiento',max_length=100,db_index=True,null=False)
    Nombre= models.CharField(verbose_name='Nombre De La Persona',max_length=100,db_index=True,null=False)
    Apellido= models.CharField(verbose_name='Apellido De La Persona', max_length=150,help_text='Coloque su apellido',null=False)
    Ciudad= models.CharField(help_text='La Ciudad En Donde Vive',max_length=200,default='Soacha',db_index=True,null=False)
    Direccion= models.CharField(help_text='Dirección de su vivienda',max_length=200,null=False)
    Telefono= models.CharField(verbose_name=' Numero De Telefono',help_text='Coloque El Numero De Celular Personal',max_length=50,unique=True,null=False)
    Correo= models.CharField(verbose_name='Correo Electronico',help_text='Escriba Su Correo Electronico Personal',max_length=200,db_index=True,null=False)
    GENERO_OPCIONES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    Genero= models.CharField(max_length=1, choices=GENERO_OPCIONES)  
    ESTADO_OPCIONES = [
        (1, 'Activo'),
        (0, 'Inactivo'),
    ]
    Activo= models.PositiveIntegerField(choices=ESTADO_OPCIONES,default=True,verbose_name='Persona Viva',help_text='Coloque el estado de la persona')  
    
    