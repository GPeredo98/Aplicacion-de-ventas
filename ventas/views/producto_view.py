from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from ventas.models.producto import Producto


class ProductoListView(generic.ListView):
    model = Producto
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ProductoListView, self).get_context_data(**kwargs)
    #     context['prueba'] = "hola mundo"
    #     return context


class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('Productos lista')


class ProductoUpdate(generic.UpdateView):
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('Productos lista')


class ProductoDelete(generic.DeleteView):
    model = Producto
    success_url = reverse_lazy('Productos lista')

