from rest_framework import serializers
from .models import Libro, Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    autores = AutorSerializer(many=True, read_only=True)

    class Meta:
        model = Libro
        fields = '__all__'
