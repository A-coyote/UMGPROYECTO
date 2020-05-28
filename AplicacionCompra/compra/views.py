from django.shortcuts import render,redirect
from .models import producto
from .models import categoria
from .forms import productos
from .forms import categorias



def inicioProductos(request):
    productos = producto.objects.all()
    contenido={
        'productos':productos
    }
    return render(request,'vistacompras.html',contenido)

def crearCompra(request):
    if request.method == 'GET':
        form= productos()
        contenido={
            'form':form
        }
    else:
        form = productos(request.POST)
        contenido={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('inicioProductos')
    return render(request,'crearCompra.html',contenido)

def editarProducto(request,id_producto):
    productoss= producto.objects.get(id_producto=id_producto)
    if request.method == 'GET':
        form=productos(instance = productoss)
        contenido={
            'form':form
        }
    else:
        form = productos(request.POST, instance = productoss)
        contenido={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('inicioProductos')
    return render(request,'crearCompra.html',contenido)

def eliminarProducto(request,id_producto):
    productos= producto.objects.get(id_producto=id_producto)
    productos.delete()
    return redirect('inicioProductos')





def crearCategoria(request):
    if request.method == 'GET':
        form= categorias()
        contenido={
            'form':form
        }
    else:
        form = categorias(request.POST)
        contenido={
            'form2':form
        }
        if form.is_valid():
            form.save()
            return redirect('inicioProductos')
    return render(request,'crearCategoria.html',contenido)

