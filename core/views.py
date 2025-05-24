from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(render, 'core/index.html')

def salute(request):
    return HttpResponse("¡Hola, mundo! Esta es la aplicación principal.")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1 style='color:blue;'>¡Hola, mundo!</h1> Esta es la aplicación principal.")

def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"¡Hola, {nombre} {apellido}!")