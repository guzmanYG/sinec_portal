# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
def index(request):
    saludito='Hola soy saludo'
    return render(request, 'sitio/index.html',{'saludo':saludito})