from django import forms

class curso_formulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class profesor_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

