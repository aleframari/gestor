# coding=utf-8
from django import forms
from .models import Actividad, Asignacion, Proyecto, Empresa
from django.contrib.auth.models import User

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields =('nombre','fecha_fin', 'prioridad', 'dificultad')
        widgets = {
            'prioridad':forms.Select,
            'dificultad': forms.Select,
}
class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields =('nombre_asignacion','empresa', 'proyectos', 'fondos','recursos_humano')
        widgets = {
            'empresa':forms.Select,
            'proyectos': forms.SelectMultiple,
}
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields =('nombre','actividades')
        widgets = {
            'actividades': forms.SelectMultiple,
}
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields =('nombre','direccion','telefono','correo')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','groups')
        widgets = {
            'password':forms.PasswordInput,
            'groups': forms.SelectMultiple,
}
class ProForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre','actividades')


def __init__ (self, *args, **kwargs):
        super(ProForm, self).__init__(*args, **kwargs)

        self.fields["actividades"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["actividades"].help_text = "Ingrese los Actores que participaron en la película"
        self.fields["actividades"].queryset = Actividad.objects.all()
