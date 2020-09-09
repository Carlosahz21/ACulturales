from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from ACulturales.models import *
from ACulturales.forms import *
from ACulturales.filters import ParroquiaFilter
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import datetime


# Pagina de inicio
def index(request):
    return render(request, "index.html")

#Listar Reporte
def listar_datos(request): 
    consulta = Agrupacion.objects.select_related("parroquia", "categoria", "ambito")
    filtro_prq = ParroquiaFilter(request.GET, queryset=consulta.all())
    consulta = filtro_prq.qs
    contexto = {"lista_agrupaciones": consulta, 
    			"filtrar_parroquias": filtro_prq}
    return render(request, "reportes.html", contexto)


def filtrar_datos(request): 
    consulta = Agrupacion.objects.select_related("parroquia", "categoria", "ambito")
    filtro_prq = ParroquiaFilter(request.GET, queryset=consulta.all())
    consulta = filtro_prq.qs
    contexto = {"lista_agrupaciones": consulta, 
    			"filtrar_parroquias": filtro_prq}
    return render(request, "ListaDatos.html", contexto)


#  Parroquias
class ParroquiaCreate(CreateView):
    model = Parroquia
    form_class = ParroquiaForm
    template_name = "parroquia_form.html"
    success_url = reverse_lazy("listar_parroquias")


class ParroquiaList(ListView):
    model = Parroquia
    template_name = "listar_parroquias.html"
    paginate_by = 5


class ParroquiaUpdate(UpdateView):
    model = Parroquia
    form_class = ParroquiaForm
    template_name = "parroquia_form.html"
    success_url = reverse_lazy("listar_parroquias")


class ParroquiaDelete(DeleteView):
    model = Parroquia
    form_class = ParroquiaForm
    template_name = "eliminar_parroquia.html"
    success_url = reverse_lazy("listar_parroquias")


# Categoria
class CategoriaCreate(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "categoria_form.html"
    success_url = reverse_lazy("listar_categorias")


class CategoriaList(ListView):
    model = Categoria
    template_name = "listar_categorias.html"
    paginate_by = 8


class CategoriaUpdate(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "categoria_form.html"
    success_url = reverse_lazy("listar_categorias")


class CategoriaDelete(DeleteView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "eliminar_categoria.html"
    success_url = reverse_lazy("listar_categorias")


# Ambito Cultural
class AmbitoCreate(CreateView):
    model = AmbitoCultural
    form_class = AmbitoForm
    template_name = "ambito_form.html"
    success_url = reverse_lazy("listar_ambitos")


class AmbitoList(ListView):
    model = AmbitoCultural
    template_name = "listar_ambitos.html"
    paginate_by = 10


class AmbitoUpdate(UpdateView):
    model = AmbitoCultural
    form_class = AmbitoForm
    template_name = "ambito_form.html"
    success_url = reverse_lazy("listar_ambitos")


class AmbitoDelete(DeleteView):
    model = AmbitoCultural
    form_class = AmbitoForm
    template_name = "eliminar_ambito.html"
    success_url = reverse_lazy("listar_ambitos")


# Agrupacion
class AgrupacionCreate(CreateView):
    model = Agrupacion
    form_class = AgrupacionForm
    template_name = "agrupacion_form.html"
    success_url = reverse_lazy("listar_agrupaciones")


class AgrupacionList(ListView):
    model = Agrupacion
    template_name = "listar_agrupaciones.html"
    paginate_by = 8


class AgrupacionUpdate(UpdateView):
    model = Agrupacion
    form_class = AgrupacionForm
    template_name = "agrupacion_form.html"
    success_url = reverse_lazy("listar_agrupaciones")


class AgrupacionDelete(DeleteView):
    model = Agrupacion
    form_class = AgrupacionForm
    template_name = "eliminar_agrupacion.html"
    success_url = reverse_lazy("listar_agrupaciones")
