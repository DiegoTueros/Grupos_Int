from django import forms
from .models import Institucion, Convenio, PlanDeCapacitacion


class InstitucionesForm(forms.ModelForm):

    class Meta:
        model = Institucion

        fields = [
            'nombre',
            'tipo',
            'descripcion',
            'paginaWeb',
            'direccion',
            'ruc',
            'distrito',
        ]
        labels = {
            'nombre': 'Nombre',
            'tipo': 'Tipo',
            'descripcion': 'Descripción',
            'paginaWeb': 'Pagina Web',
            'direccion': 'Dirección',
            'ruc': 'RUC',
            'distrito': 'Distrito',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'paginaWeb': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'distrito': forms.Select(attrs={'class': 'form-control'}),
        }


class ConveniosForm(forms.ModelForm):

    class Meta:
        model = Convenio

        fields = [
            'escuela',
            'institucion',
            'tipo',
            'fechaInicio',
            'fechaFin',
        ]
        labels = {
            'escuela': 'Escuela',
            'institucion': 'Institución',
            'tipo': 'Tipo',
            'fechaInicio': 'Fecha Inicial',
            'fechaFin': 'Fecha Final',
        }

        widgets = {
            'escuela': forms.Select(attrs={'class': 'form-control'}),
            'institucion': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaInicio': forms.DateInput(attrs={'class': 'form-control'}),
            'fechaFin': forms.DateInput(attrs={'class': 'form-control'}),

        }

class PlanCapForm(forms.ModelForm):

    class Meta:
        model = PlanDeCapacitacion

        fields = [
            'convenio',
            'denominacion',
        ]
        labels = {
            'convenio': 'Convenio',
            'denominacion': 'Denominación',
        }

        widgets = {
            'convenio': forms.Select(attrs={'class': 'form-control'}),
            'denominacion': forms.TextInput(attrs={'class': 'form-control'}),
        }
