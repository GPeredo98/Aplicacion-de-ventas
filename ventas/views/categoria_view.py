from django.urls import reverse_lazy
from django.views import generic

from ventas.models.categoria import Categoria


class CategoriaListView(generic.ListView):
    model = Categoria


class CategoriaCreate(generic.CreateView):
    model = Categoria
    fields = '__all__'
    success_url = reverse_lazy('Categoria lista')


class CategoriaUpdate(generic.UpdateView):
    model = Categoria
    fields = '__all__'
    success_url = reverse_lazy('Categoria lista')


class CategoriaDelete(generic.DeleteView):
    model = Categoria
    success_url = reverse_lazy('Categoria lista')
