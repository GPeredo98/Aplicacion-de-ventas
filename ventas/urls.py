from django.urls import path
from ventas.views import producto_view, venta_view, categoria_view

urlpatterns = [
    path('', venta_view.index, name="Index"),
    path('realizar_venta', venta_view.realizar_venta, name="Realizar venta"),
    path('ventas_lista', venta_view.VentaListView.as_view(), name="Ventas lista"),
    path('venta_editar/<int:pk>', venta_view.VentaUpdate.as_view(), name="Ventas editar"),
    path('ver_detalle_venta/<int:pk>', venta_view.ver_detalle_venta, name="Ver detalle venta"),

    path('busqueda', venta_view.busqueda, name="Busqueda"),
    path('productos_lista', producto_view.ProductoListView.as_view(), name="Productos lista"),
    path('producto_crear', producto_view.ProductoCreate.as_view(), name="Producto crear"),
    path('producto_editar/<int:pk>', producto_view.ProductoUpdate.as_view(), name="Producto editar"),
    path('producto_eliminar/<int:pk>', producto_view.ProductoDelete.as_view(), name="Producto eliminar"),

    path('categoria_lista', categoria_view.CategoriaListView.as_view(), name="Categoria lista"),
    path('categoria_crear', categoria_view.CategoriaCreate.as_view(), name="Categoria crear"),
    path('categoria_editar/<int:pk>', categoria_view.CategoriaUpdate.as_view(), name="Categoria editar"),
    path('categoria_eliminar/<int:pk>', categoria_view.CategoriaDelete.as_view(), name="Categoria eliminar"),

    path('anular_venta', venta_view.anular_venta, name="Anular venta"),
    path('emitir_factura', venta_view.emitir_factura, name="Emitir factura"),
]