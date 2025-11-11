from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Curso, Profesor, Estudiante, Entregable
from django.contrib import messages

def home(request):
    resultados = []
    mensaje = None

    if 'camada' in request.GET:
        query = request.GET.get('camada')
        if query:
            resultados = Curso.objects.filter(camada=query)
            if not resultados:
                mensaje = f"No existe ninguna camada con el número {query}."
        else:
            mensaje = "Por favor, ingresa un número de camada."

    return render(request, 'home.html', {
        'resultados': resultados,
        'mensaje': mensaje
    })

def profesor_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        profesion = request.POST.get("profesion")

        Profesor.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            profesion=profesion
        )

        return render(request, "profesor_form.html", {"success": True})

    return render(request, "profesor_form.html")

from .models import Curso

def curso_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        camada = request.POST.get("camada")

        Curso.objects.create(
            nombre=nombre,
            camada=camada
        )
        return render(request, "blog/curso_form.html", {"success": True})
    
    return render(request, "blog/curso_form.html")

def estudiante_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")

        Estudiante.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email
        )
        return render(request, "blog/estudiante_form.html", {"success": True})
    
    return render(request, "blog/estudiante_form.html")

def entregable_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        fecha_entrega = request.POST.get("fecha_entrega")
        entregado = request.POST.get("entregado") == "on"

        Entregable.objects.create(
            nombre=nombre,
            fecha_entrega=fecha_entrega,
            entregado=entregado
        )
        return render(request, "blog/entregable_form.html", {"success": True})
    
    return render(request, "blog/entregable_form.html")