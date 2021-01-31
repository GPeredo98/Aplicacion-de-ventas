from django.db import models

from ventas.models.categoria import Categoria


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300)
    precio_actual = models.DecimalField(max_digits=50, decimal_places=2)
    stock_actual = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(blank=True, upload_to='images')
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='Categoria', null=False)

    class Meta:
        db_table = 'ventas_productos'

    def __str__(self):
        return self.nombre + ' - ' + str(self.precio_actual)


class ImagenProducto(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(blank=True, upload_to='images')
    fk_producto = models.ForeignKey(Producto, models.CASCADE)

    class Meta:
        db_table = 'ventas_imagen_producto'
