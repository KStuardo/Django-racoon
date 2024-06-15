
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Producto

# Create your views here.
#esto se copia por cada pagina colocando la raiz correspondiente 
def index(request):
    template=loader.get_template('formulario/index.html')
    return HttpResponse(template.render())


def Carrito(request):
    template=loader.get_template('paginas/Carrito.html')
    return HttpResponse(template.render())

def ciberseguridad(request):
    template=loader.get_template('paginas/ciberseguridad.html')
    return HttpResponse(template.render())

def IA(request):
    template=loader.get_template('paginas/IA.html')
    return HttpResponse(template.render())


def MisionVision(request):
    template=loader.get_template('paginas/MisionVision.html')
    return HttpResponse(template.render())

def noticiasDuoc(request):
    template=loader.get_template('paginas/noticiasDuoc.html')
    return HttpResponse(template.render())

def pago2(request):
     template=loader.get_template('paginas/ pago2.html')
     return HttpResponse(template.render())