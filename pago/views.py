# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import cohorte1

def busqueda_productos(request):
    return render(request,'busqueda_productos.html')

def buscar(request):
    try:
        estudiante = cohorte1.objects.get(CI = request.GET['pdr'])
        
        return render(request,'aceptado.html', {
            'estudiante': estudiante,
        })

    except cohorte1.DoesNotExist:
        return render(request,'rechazo.html')
        
 




