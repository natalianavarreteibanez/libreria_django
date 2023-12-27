"""
URL configuration for templatesDemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from templatesApp.views import *
from templatesApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from templatesApp.views import AutorList, AutorDetail, LibroList, LibroDetail




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sistema_administrador, name='sistema_administrador'),
    path('agregar/', agregar_libro, name='agregar_libro'),
    path('lista-libros/', lista_libros, name='lista_libros'),
    path('agregar-autor/', agregar_autor, name='agregar_autor'),  # Nueva ruta para agregar autor
    path('lista-autores/', lista_autores, name='lista_autores'),  # Ruta para ver lista de autores
    path('eliminarProyecto/<int:id>', eliminarProyecto, name='eliminarProyecto'),
    path('actualizarProyecto/<int:id>', actualizarProyecto, name='actualizarProyecto'),
    path('ver-archivo/<int:libro_id>/', views.ver_archivo, name='ver_archivo'),
    path('actualizar_autor/<int:autor_id>/', views.actualizar_autor, name='actualizar_autor'),
    path('eliminar_autor/<int:autor_id>/', views.eliminar_autor, name='eliminar_autor'),
    path('autores/', AutorList.as_view(), name='autor-list'),
    path('autores/<int:pk>/', AutorDetail.as_view(), name='autor-detail'),
    path('libros/', LibroList.as_view(), name='libro-list'),
    path('libros/<int:pk>/', LibroDetail.as_view(), name='libro-detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)