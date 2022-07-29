from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class curso_formulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class profesor_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label= "Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label= "Repite la contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model= User
        fields = ['username',"email", "password1", "password2", 'last_name', 'first_name']
        help_texts= {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = ['email', 'password1', 'password2' ]
        help_texts= {k: "" for k in fields}

