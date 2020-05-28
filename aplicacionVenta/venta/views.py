from django.shortcuts import render,redirect
from .models import venta_det
from .forms import ventas
from AplicacionCompra.compra.models import producto



def vistaVentas(request):
    ventas = venta_det.objects.all()
    contenido={
        'ventas':ventas
    }
    return render(request,'vistaVentas.html',contenido)

#facturacion
def vistafact(request):
    ventas = venta_det.objects.all()
    contenido={
        'ventas':ventas
    }
    return render(request,'factura.html',contenido)

def generaVenta(request):
    if request.method == 'GET':
        form= ventas()
        contenido={
            'form':form
        }
    else:
        form = ventas(request.POST)
        contenido={
            'form':form

        }
        if form.is_valid():
            form.save()
            return redirect('generaVenta')
    return render(request,'crearVenta.html',contenido)


def editarVenta(request,id_venta):
    ventass= venta_det.objects.get(id_venta=id_venta)
    if request.method == 'GET':
        form=ventas(instance = ventass)
        contenido={
            'form':form
        }
    else:
        form = ventas(request.POST, instance = ventass)
        contenido={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('generaVenta')
    return render(request,'crearVenta.html',contenido)


def eliminarVenta(request,id_venta):
    ventas= venta_det.objects.get(id_venta=id_venta)
    ventas.delete()
    return redirect('vistaVentas')





