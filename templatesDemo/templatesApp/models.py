from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.CharField(max_length=1000)
    foto = models.FileField(upload_to='archivos_autor/')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    editorial = models.CharField(max_length=50)
    anio_publicacion = models.IntegerField()
    archivo = models.FileField(upload_to='archivos_libros/')
    autores = models.ManyToManyField(Autor)  # Relación muchos a muchos con Autor

    def __str__(self):
        return self.titulo

