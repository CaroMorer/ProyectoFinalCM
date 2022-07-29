from typing import List
from django.http.request import QueryDict
from django.http import HttpResponse, QueryDict
from django.shortcuts import render, HttpResponse
from AppCoder.models import Curso, Profesor
from AppCoder.forms import curso_formulario, profesor_formulario, UserRegisterForm, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
def curso(request):
    curso = Curso(nombre = "Datos", camada = "22")
    curso.save()
    curso2 = Curso(nombre="Marketing", camada="247")
    curso2.save()

    documento_texto = f"--Curso1: {curso.nombre}, Camada: {curso.camada}, ---Curso2: {curso2.nombre} Camada: {curso2.camada}"
    return HttpResponse(documento_texto)

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def cursos(request):

    if request.method == 'POST':

        mi_formulario = curso_formulario(request.POST) 

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            curso = Curso (nombre = informacion['curso'], camada = informacion['camada'])
            
            curso.save()

            return render(request, 'AppCoder/inicio.html')

    else:

        mi_formulario = curso_formulario()

    return render(request, 'AppCoder/cursos.html', {'mi_formulario': mi_formulario })

def profesores(request):
    if request.method == 'POST':

        mi_formulario = profesor_formulario(request.POST) 

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            profesor = Profesor (nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'], profesion=informacion['profesion'])
            
            profesor.save()

            return render(request, 'AppCoder/inicio.html')

    else:

        mi_formulario = profesor_formulario()

    return render(request, 'AppCoder/profesores.html', {'mi_formulario': mi_formulario })

def buscar(request):

    if request.GET['camada']:

        camada = request.GET['camada']
        print(camada)
        cursos = Curso.objects.filter(camada__icontains= camada)
        print(cursos)
        return render(request, 'AppCoder/inicio.html', {'cursos': cursos,'camada':camada})
    else:
        respuesta = 'No enviaste datos'

    return render(request, 'AppCoder/inicio.html', {'respuesta':respuesta})

def leer_profesores(request):

    profesores = Profesor.objects.all()

    contexto = {"profesores": profesores}

    return render(request, 'AppCoder/leer_profesores.html', contexto)

def eliminar_profesor(request, profesor_nombre):

    profesor = Profesor.objects.get(nombre=profesor_nombre)

    profesor.delete()

    profesores = Profesor.objects.all()
    
    contexto= {'profesores': profesores}

    return render(request, 'AppCoder/leer_profesores.html', contexto)

def editar_profesor(request, profesor_nombre):

    profesor = Profesor.objects.get(nombre=profesor_nombre)

    if request.method == "POST" :

        mi_formulario = profesor_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesión = informacion['profesion']

            profesor.save()

            return render(request, 'AppCoder/inicio.html')
    else:
        mi_formulario= profesor_formulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion})
    return render(request, 'AppCoder/editar_profesor.html', {'mi_formulario': mi_formulario, 'profesor_nombre': profesor_nombre }) 

class CursoList(LoginRequiredMixin, ListView):
    
    model = Curso
    template_name= "AppCoder/cursos_list.html"

class CursoDetalle(DetailView):
    
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):

    model = Curso 
    success_url = "/AppCoder/curso/list"
    fields = [ 'nombre', 'camada']

class CursoUpdate(UpdateView):

    model = Curso 
    success_url = "/AppCoder/curso/list"
    fields = [ 'nombre', 'camada']

class CursoDelete(DeleteView):
    model = Curso
    success_url ="/AppCoder/curso/list"

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user =authenticate(username=usuario, password=contra)

            if user is not None:
                login(request,user)

                return render(request, "AppCoder/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                
                return render(request,"AppCoder/inicio.html", {"mensaje": f"Error, datos incorrectos"})

        else:
            return render(request,"AppCoder/inicio.html", {"mensaje": "Error, formulario erroneo"})
    form = AuthenticationForm()
    return render(request,"AppCoder/login.html", {"form": form})


def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":"Usuario Creado: )"})

    else:
        form = UserCreationForm()
    return render(request, "AppCoder/registro.html", {"form":form})

@login_required
def editar_perfil(request):
     usuario = request.user

     if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)
        if mi_formulario.is_valid():

            informacion=mi_formulario.cleaned_data

            usuario.email= informacion ['email']
            usuario.pasword1= informacion ['pasword1']
            usuario.pasword2= informacion ['pasword2']
            usuario.save()

            return render(request, 'AppCoder/inicio.html')
            
     else: 
        mi_formulario=UserEditForm(initial={'email':usuario.email})

        return render(request,"AppCoder/editar_perfil.html", {"mi_formulario":mi_formulario, "usuario": usuario})        

