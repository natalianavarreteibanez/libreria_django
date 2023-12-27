from django import forms
from .models import Libro, Autor

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
    
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn.isdigit() or len(isbn) != 13:
            raise forms.ValidationError("El ISBN debe ser un número de 13 dígitos.")
        return isbn

class AutorForm(forms.ModelForm):  # Corregido el nombre de la clase a AutorForm
    class Meta:
        model = Autor
        fields = '__all__'
