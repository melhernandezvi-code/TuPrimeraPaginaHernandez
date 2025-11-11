from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profesores/', views.profesor_form, name='profesor_form'),
    path('cursos/', views.curso_form, name='curso_form'),
    path('estudiantes/', views.estudiante_form, name='estudiante_form'),
    path('entregables/', views.entregable_form, name='entregable_form'),
]