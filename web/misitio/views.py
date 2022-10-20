from django.shortcuts import render
from .models import Cliente
from django.utils import timezone
# Create your views here.

def clientes_list(request):
    clientes = Cliente.objects.filter(fechalta__lte=timezone.now()).order_by('fechalta')
    return render(request, 'misitio/clientes_list.html', {'clientes': clientes})