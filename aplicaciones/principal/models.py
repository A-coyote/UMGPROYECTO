from django.db import models

#Tabla clientes en nuestra base de datos
class cliente(models.Model):
    id_cliente = models.AutoField(primary_key = True)
    nombre_cliente = models.CharField(max_length = 50, unique = True)
    apellido_cliente = models.CharField(max_length=50)
    direccion_cliente = models.CharField(max_length=70)
    telefono_cliente = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_cliente


