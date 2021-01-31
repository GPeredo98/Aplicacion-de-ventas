from django.db import models

from ventas.models.producto import Producto
from ventas.models.venta import Venta


class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    fk_venta = models.ForeignKey(Venta, on_delete=models.CASCADE,related_name='Venta', null=False)
    fk_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='Producto', null=False)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        db_table = 'ventas_detalles_ventas'

    def __str__(self):
        return self.fk_venta + ' - ' + self.fk_producto + ' - ' + self.cantidad
