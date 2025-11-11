from django import forms
from .models import Profesor, Curso, Estudiante, Entregable

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']

class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_entrega', 'entregado']
        widgets = {
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_entregado(self):
        entregado = self.cleaned_data.get('entregado')
        if not entregado:
            raise forms.ValidationError("Debe marcar 'Entregado' antes de enviar.")
        return entregado
