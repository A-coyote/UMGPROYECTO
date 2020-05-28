from django.db import models
#from aplicacionVenta.venta.models import venta_det



#Tabla CATEGORIA en nuestra base de datos
class categoria(models.Model):
    id_categoria = models.AutoField(primary_key = True)
    nombre_categoria = models.CharField(max_length = 50, unique=True)
    descripcion_categoria= models.CharField(max_length =250)

    def __str__(self):
        return self.nombre_categoria


#Tabla Producto en nuestra base de datos
class producto(models.Model):
    id_producto = models.AutoField(primary_key = True)
    nombre_producto = models.CharField(max_length = 50, unique=True)
    precio_prod = models.FloatField()
    cantidad_prod = models.PositiveIntegerField(blank=True, null=True)
    id_categoria_id = models.ForeignKey(categoria, on_delete=models.CASCADE)

   
 
    def __str__(self):
        return self.nombre_producto



