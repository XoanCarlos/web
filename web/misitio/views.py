from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm
from django.utils import timezone
from django.views.generic import CreateView
# Create your views here.

def clientes_list(request):
    clientes = Cliente.objects.filter(fechalta__lte=timezone.now()).order_by('fechalta')
    return render(request, 'misitio/clientes_list.html', {'clientes': clientes})

def cliente_new(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            cliente.save()
    else:
        form = ClienteForm()
    return render(request, 'misitio/cliente_edit.html', {'form': form})
