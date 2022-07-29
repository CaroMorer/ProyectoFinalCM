from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name = 'Inicio'),
    path('cursos', views.cursos, name = 'Cursos'),
    path('profesores', views.profesores, name = 'Profesores'),
    path('estudiantes', views.estudiantes, name = 'Estudiantes'),
    path('entregables', views.entregables, name = 'Entregables'),
    path('curso_formulario', views.cursos, name = 'curso_formulario'),
    path('profesor_formulario', views.profesores, name = 'profesor_formulario'),
    path('buscar/', views.buscar),
    path('leer_profesores', views.leer_profesores, name = "leer_profesores"),
    path('eliminar_profesor/<profesor_nombre>/', views.eliminar_profesor, name="eliminar_profesor"),
    path('editar_profesor/<profesor_nombre>/', views.editar_profesor, name='editar_profesor'),
    path('curso/list', views.CursoList.as_view(), name = 'List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    path('login', views.login_request, name = 'Login'),
    path('registro', views.register, name = 'Registro'),
    path('logout', LogoutView.as_view(template_name="AppCoder/logout.html"), name= "logout" ),
    path('editar_perfil', views.editar_perfil, name = 'EditarPerfil'),


    ]