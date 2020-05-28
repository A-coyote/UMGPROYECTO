from django.shortcuts import render,redirect
from .models import cliente
from .forms import  clientes

def inicio(request):
    clientes = cliente.objects.all()
    contenido={
        'clientes':clientes
    }
    return render(request,'index.html',contenido)

def crear(request):
    if request.method == 'GET':
        form= clientes()
        contenido={
            'form':form
        }
    else:
        form = clientes(request.POST)
        contenido={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crearCliente.html',contenido)

def editar(request,id_cliente):
    clientess= cliente.objects.get(id_cliente=id_cliente)
    if request.method == 'GET':
        form=clientes(instance = clientess)
        contenido={
            'form':form
        }
    else:
        form = clientes(request.POST, instance = clientess)
        contenido={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crearCliente.html',contenido)

def eliminarCliente(request,id_cliente):
    clientes= cliente.objects.get(id_cliente=id_cliente)
    clientes.delete()
    return redirect('index')