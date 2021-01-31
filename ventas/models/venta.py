from django.db import models
from django_fsm import FSMIntegerField, transition

# from ventas.models.detalle_venta import DetalleVenta


class Venta(models.Model):

    ESTADO_CREADO = 0
    ESTADO_PAGADO = 1
    ESTADO_FACTURADO = 2
    ESTADO_FINALIZADO = 3
    ESTADO_CANCELADO = -1
    ESTADO_ANULADO = -2

    ESTADOS = (
        (ESTADO_CREADO, 'creado'),
        (ESTADO_PAGADO, 'pagado'),
        (ESTADO_FACTURADO, 'facturado'),
        (ESTADO_FINALIZADO, 'finalizado'),
        (ESTADO_CANCELADO, 'cancelado'),
        (ESTADO_ANULADO, 'anulado'),
    )

    id = models.AutoField(primary_key=True)
    codigo = models.IntegerField(null=False)
    fecha_hora = models.DateTimeField()
    total = models.DecimalField(max_digits=50, decimal_places=2, null=False)
    estado = FSMIntegerField(choices=ESTADOS, default=ESTADO_CREADO, protected=True)
    factura_nombre = models.CharField(null=True, max_length=100)
    factura_nit = models.IntegerField(null=True)
    motivo_anulacion = models.CharField(max_length=400, null=True)

    class Meta:
        db_table = 'ventas_ventas'

    @transition(estado, source=ESTADO_CREADO, target=ESTADO_PAGADO)
    def pagar(self):
        pass

    @transition(estado, source=ESTADO_PAGADO, target=ESTADO_FACTURADO)
    def facturar(self, nombre, nit):
        self.factura_nombre = nombre
        self.factura_nit = nit
        pass

    @transition(estado, source=[ESTADO_PAGADO, ESTADO_FACTURADO], target=ESTADO_FINALIZADO)
    def finalizar(self):
        pass

    @transition(estado, source=ESTADO_CREADO, target=ESTADO_CANCELADO)
    def cancelar(self):
        pass

    @transition(estado, source=[ESTADO_FINALIZADO, ESTADO_PAGADO, ESTADO_FACTURADO], target=ESTADO_ANULADO)
    def anular(self, motivo):
        self.motivo_anulacion = motivo
        pass
