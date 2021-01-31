from datetime import datetime

import pytz
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
import json

from ventas.models.detalle_venta import DetalleVenta
from ventas.models.producto import Producto
from ventas.models.venta import Venta


def index(request):
    return render(request, 'inicio.html')


def busqueda(request):
    if request.GET['nombre'] is not "":
        if Producto.objects.filter(nombre__startswith=request.GET['nombre']).first() is not None:
            productos = Producto.objects.filter(nombre__startswith=request.GET['nombre']).values(
                'id', 'nombre', 'precio_actual')
        else:
            productos = []
    else:
        productos = []
    for producto in productos:
        producto['precio_actual'] = str(producto['precio_actual'])

    return HttpResponse(json.dumps(list(productos)))


def realizar_venta(request):
    venta = Venta()
    venta.codigo = 200
    venta.fecha_hora = datetime.now(pytz.timezone('America/La_Paz'))
    venta.total = request.GET['total']
    venta.save()
    venta.codigo = 200 + venta.id
    venta.pagar()
    venta.save()
    for x in range(int((request.GET.__len__()-1)/2)):
        prod = Producto.objects.get(id=request.GET.get('carrito['+str(x)+'][id]'))
        detalle_venta = DetalleVenta()
        detalle_venta.fk_venta = venta
        detalle_venta.fk_producto = prod
        detalle_venta.cantidad = request.GET.get('carrito['+str(x)+'][cantidad]')
        detalle_venta.precio = int(request.GET.get('carrito['+str(x)+'][cantidad]')) * prod.precio_actual
        detalle_venta.save()

    return HttpResponse(venta.id)


class VentaUpdate(generic.UpdateView):
    model = Venta
    fields = '__all__'
    success_url = reverse_lazy('Ventas lista')


class VentaListView(generic.ListView):
    model = Venta


def ver_detalle_venta(request, pk):
    venta = Venta.objects.get(id=pk)
    lista_detalles = DetalleVenta.objects.filter(fk_venta=pk)
    return render(request, 'detalle_venta.html', {
        'venta': venta,
        'lista_detalles': lista_detalles
    })


def anular_venta(request):
    venta = Venta.objects.get(id=request.GET['venta_id'])
    venta.anular(request.GET['motivo'])
    venta.save()
    return HttpResponse(request.GET)


def emitir_factura(request):
    venta = Venta.objects.get(id=request.GET['venta_id'])
    venta.facturar(request.GET['factura_nombre'], request.GET['factura_nit'])
    venta.save()
    return HttpResponse('gg')
