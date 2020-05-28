from django.db import models
from aplicaciones.principal.models import cliente
from AplicacionCompra.compra.models import producto
#Tabla Producto en nuestra base de datos

class venta_det(models.Model):
    id_venta = models.AutoField(primary_key = True)
    fecha_venta = models.DateField(auto_now=True)  #auto_now=True
    id_cliente_id= models.ForeignKey(cliente, on_delete=models.CASCADE)
    id_producto_id = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.FloatField()
    total = models.FloatField(editable=False)

   

    def save(self, *args, **kwargs):
        self.total = self.cantidad * self.precio
        super(venta_det,self).save(*args, **kwargs)

    
    def __int__(self):
        return self.id_venta


