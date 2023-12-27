
from django.shortcuts import render, get_object_or_404, redirect

from templatesDemo import settings
from .models import Libro, Autor
from .forms import LibroForm, AutorForm
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
import os



def sistema_administrador(request):
    return render(request, 'sistema_administrador.html')


def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'detalle_libro.html', {'libro': libro})


def eliminarProyecto(request, id):
    try:
        proyecto = Libro.objects.get(id=id)
    except Libro.DoesNotExist:
        raise Http404("El libro no existe o fue eliminado previamente.")
    
    proyecto.delete()
    return redirect('lista_libros')

def actualizarProyecto(request, id):
    proyecto = Libro.objects.get(id = id)
    form = LibroForm(instance=proyecto)
    if request.method == "POST" : 
        form = LibroForm(request.POST, instance=proyecto)
        if form.is_valid() :
            form.save()
        return sistema_administrador(request)
    data= {'form' : form}
    return render(request, 'agregar_libro.html', data)

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')  # Redirige a la lista de autores después de agregar uno nuevo
    else:
        form = AutorForm()
    return render(request, 'agregar_autor.html', {'form': form})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'lista_autor.html', {'autores': autores})

def detalle_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    return render(request, 'detalle_autor.html', {'autor': autor})

def eliminar_autor(request, autor_id):  # Debe coincidir con el nombre del argumento en la URL
    try:
        autor = Autor.objects.get(id=autor_id)  # Utiliza el nombre del argumento correcto
    except Autor.DoesNotExist:
        raise Http404("El autor no existe o fue eliminado previamente.")
    
    autor.delete()
    return redirect('lista_autores')  # Redirige a la lista de autores después de eliminar


def actualizar_autor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    form = AutorForm(instance=autor)
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')  # Redirige a la lista de autores después de actualizar
    data = {'form': form}
    return render(request, 'agregar_autor.html', data)


def ver_archivo(request, libro_id):
    try:
        libro = Libro.objects.get(pk=libro_id)
        if libro.imagen_libro:
            imagen_path = os.path.join(settings.MEDIA_ROOT, 'archivos_libros', libro.imagen.name)
            with open(imagen_path, 'rb') as image_file:
                return HttpResponse(image_file.read(), content_type='image/jpeg')  # O el tipo de imagen que estés utilizando (image/png, etc.)
        else:
            return HttpResponse("Imagen no encontrada")  # O maneja el caso cuando no haya imagen
    except Libro.DoesNotExist:
        return HttpResponse("El libro no existe")
    
    
    
# VISTAS PARA LA API DE DJANGO REST FRAMEWORK
from rest_framework import generics, permissions
from .models import Libro, Autor
from .serializers import LibroSerializer, AutorSerializer

class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LibroList(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LibroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
