"""webAC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ACulturales.views import *

urlpatterns = [
    path('', index, name="index"),
    path('reportes/', listar_datos, name="listar_reporte"),
    path('filtro/', filtrar_datos, name="filtrar"),
    path('admin/', admin.site.urls, name="admin"),
    path('parroquias/', ParroquiaList.as_view(), name="listar_parroquias"),
    path('parroquias/crear/', ParroquiaCreate.as_view(), name="crear_parroquia"),
    path('parroquias/actualizar/<int:pk>', ParroquiaUpdate.as_view(), name="editar_parroquia"),
    path('parroquias/eliminar/<int:pk>', ParroquiaDelete.as_view(), name="eliminar_parroquia"),
    path('categorias/', CategoriaList.as_view(), name="listar_categorias"),
    path('categorias/crear/', CategoriaCreate.as_view(), name="crear_categoria"),
    path('categorias/actualizar/<int:pk>', CategoriaUpdate.as_view(), name="editar_categoria"),
    path('categorias/eliminar/<int:pk>', CategoriaDelete.as_view(), name="eliminar_categoria"), 
    path('ambitos/', AmbitoList.as_view(), name="listar_ambitos"),
    path('ambitos/crear/', AmbitoCreate.as_view(), name="crear_ambito"),
    path('ambitos/actualizar/<int:pk>', AmbitoUpdate.as_view(), name="editar_ambito"),
    path('ambitos/eliminar/<int:pk>', AmbitoDelete.as_view(), name="eliminar_ambito"),
    path('agrupaciones/', AgrupacionList.as_view(), name="listar_agrupaciones"),
    path('agrupaciones/crear/', AgrupacionCreate.as_view(), name="crear_agrupacion"),
    path('agrupaciones/actualizar/<int:pk>', AgrupacionUpdate.as_view(), name="editar_agrupacion"),
    path('agrupaciones/eliminar/<int:pk>', AgrupacionDelete.as_view(), name="eliminar_agrupacion")
]
