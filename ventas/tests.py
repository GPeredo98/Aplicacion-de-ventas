from django.test import TestCase

# Create your tests here.
from django.utils import timezone

from ventas.models.categoria import Categoria
from ventas.models.detalle_venta import DetalleVenta
from ventas.models.producto import Producto
from ventas.models.venta import Venta
from ventas.views import venta_view


class TestCategoria(TestCase):
    def test_categoria(self):
        categoria_1 = Categoria.objects.create(nombre='Frutas')
        categoria_1.save()
        categoria_2 = Categoria.objects.create(nombre='Verduras')
        categoria_2.save()

        categoria_test_1 = Categoria.objects.filter(nombre='Frutas').first()
        categoria_test_2 = Categoria.objects.filter(nombre='Manzanas').first()

        self.assertIsNotNone(categoria_test_1, "Fail: No se encontró la categoria creada")
        self.assertIsNone(categoria_test_2, "Fail: Se encontró una categoria que no existe")
        self.assertEquals(categoria_test_1.nombre, "Frutas", "Fail: No es el mismo nombre")
        self.assertNotEqual(categoria_1.id, categoria_2.id, "Fail: Categorias con el mismo id")


class TestProducto(TestCase):
    def test_producto(self):
        categoria_1 = Categoria.objects.create(nombre='Frutas')
        categoria_2 = Categoria.objects.create(nombre='Verduras')
        categoria_1.save()
        categoria_2.save()

        producto_1 = Producto.objects.create(
            nombre='Papaya', descripcion='--', precio_actual=15, stock_actual=200, fk_categoria=categoria_1)
        producto_2 = Producto.objects.create(
            nombre='Cebolla', descripcion='--', precio_actual=5, stock_actual=20, fk_categoria=categoria_2)
        producto_1.save()
        producto_2.save()

        producto_test_1 = Producto.objects.filter(nombre='Papaya').first()
        producto_test_2 = Producto.objects.filter(nombre='Tomate').first()

        self.assertIsNotNone(producto_test_1, "Fail: No se encontró la categoria creada")
        self.assertIsNone(producto_test_2, "Fail: Se encontró una categoria que no existe")
        self.assertEquals(producto_test_1.nombre, "Papaya", "Fail: No es el mismo nombre")
        self.assertNotEqual(producto_1.id, producto_2.id, "Fail: Categorias con el mismo id")


class TestVenta(TestCase):
    def test_venta(self):
        categoria_1 = Categoria.objects.create(nombre='Frutas')
        categoria_2 = Categoria.objects.create(nombre='Verduras')
        categoria_1.save()
        categoria_2.save()

        producto_1 = Producto.objects.create(
            nombre='Papaya', descripcion='--', precio_actual=15, stock_actual=200, fk_categoria=categoria_1)
        producto_2 = Producto.objects.create(
            nombre='Cebolla', descripcion='--', precio_actual=5, stock_actual=20, fk_categoria=categoria_2)
        producto_1.save()
        producto_2.save()

        venta_1 = Venta.objects.create(codigo=221, fecha_hora=timezone.now(), total=10)
        venta_1.save()
        venta_2 = Venta.objects.create(codigo=222, fecha_hora=timezone.now(), total=20)
        venta_2.save()
        venta_3 = Venta.objects.create(codigo=223, fecha_hora=timezone.now(), total=30)
        venta_3.save()
        venta_4 = Venta.objects.create(codigo=224, fecha_hora=timezone.now(), total=40)
        venta_4.save()
        venta_5 = Venta.objects.create(codigo=225, fecha_hora=timezone.now(), total=50)
        venta_5.save()

        detalle_venta_1 = DetalleVenta.objects.create(
            fk_venta=venta_1, fk_producto=producto_1, cantidad=2, precio=producto_1.precio_actual * 2)
        detalle_venta_2 = DetalleVenta.objects.create(
            fk_venta=venta_2, fk_producto=producto_2, cantidad=2, precio=producto_2.precio_actual * 2)
        detalle_venta_3 = DetalleVenta.objects.create(
            fk_venta=venta_3, fk_producto=producto_1, cantidad=2, precio=producto_1.precio_actual * 2)
        detalle_venta_4 = DetalleVenta.objects.create(
            fk_venta=venta_4, fk_producto=producto_2, cantidad=2, precio=producto_2.precio_actual * 2)
        detalle_venta_1.save()
        detalle_venta_2.save()
        detalle_venta_3.save()
        detalle_venta_4.save()

        venta_2.pagar()
        venta_2.save()

        venta_3.pagar()
        venta_3.facturar("Gabriel Peredo", 8143502011)
        venta_3.save()

        venta_4.pagar()
        venta_4.anular("Este es un motivo")
        venta_4.save()

        venta_test_1 = Venta.objects.filter(codigo=221).first()
        venta_test_2 = Venta.objects.filter(codigo=10).first()

        self.assertIsNotNone(venta_test_1, "Fail: No se encontró la categoria creada")
        self.assertIsNone(venta_test_2, "Fail: Se encontró una categoria que no existe")
        self.assertEquals(venta_1.codigo, 221, "Fail: No es el mismo codigo")
        self.assertNotEqual(venta_1.id, venta_2.id, "Fail: Categorias con el mismo id")
        self.assertEqual(venta_1.estado, 0, "Fail: El estado de la venta no es 0")
        self.assertEqual(venta_2.estado, 1, "Fail: El estado de la venta no es 1")
        self.assertEqual(venta_3.estado, 2, "Fail: El estado de la venta no es 2")
        self.assertEqual(venta_4.estado, -2, "Fail: El estado de la venta no es -2")
