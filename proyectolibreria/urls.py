"""proyectolibreria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicaciones.principal.views import inicio,crear,editar,eliminarCliente
from AplicacionCompra.compra.views import inicioProductos,crearCompra,crearCategoria,editarProducto,eliminarProducto
from aplicacionVenta.venta.views import vistaVentas,generaVenta,editarVenta,eliminarVenta,vistafact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name = 'index'),
    path('crearCliente/',crear,name ='crearCliente'),
    path('editar/<int:id_cliente>/',editar,name='editarcliente'),
    path('eliminarCliente/<int:id_cliente>/',eliminarCliente,name='eliminar'),
    path('inicioProductos',inicioProductos,name = 'inicioProductos'),
    path('crearCompra/',crearCompra, name='crearCompra'),
    path('crearCategoria/',crearCategoria, name='crearCategoria'),
    path('editarProducto/<int:id_producto>/',editarProducto,name='editarProducto'),
    path('eliminarProducto/<int:id_producto>/',eliminarProducto,name='eliminarProducto'),
    path('vistaVentas/',vistaVentas,name='vistaVentas'),
    path('generaVenta/',generaVenta,name='generaVenta'),
    path('editarVenta/<int:id_venta>/',editarVenta,name='editarVenta'),
    path('eliminarVenta/<int:id_venta>/',eliminarVenta,name='eliminarVenta'),
    path('vistafact/',vistafact,name='vistafact')
]
