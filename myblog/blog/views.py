from django.shortcuts import render
from .models import Sobre, Curso, Interesse

def index(request):
    sobre = Sobre.objects.first()
    cursos = Curso.objects.all()
    interesses = Interesse.objects.all()
    return render(request, 'index.html', {
        'sobre': sobre,
        'cursos': cursos,
        'interesses': interesses
    })

def sobre_mim(request):
    sobre = Sobre.objects.first()
    return render(request, 'sobre_mim.html', {'sobre': sobre})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def interesses(request):
    interesses = Interesse.objects.all()
    return render(request, 'interesses.html', {'interesses': interesses})
