from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto, Orden, DetalleOrden
from .carrito import Carrito

# 1. Vista del Catálogo
def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/catalogo.html', {'productos': productos})

# 2. Vistas de control del Carrito
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.agregar(producto)
    messages.success(request, f'¡{producto.nombre} agregado al carrito!')
    return redirect('catalogo')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.restar(producto)
    return redirect('ver_carrito')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.eliminar(producto)
    messages.warning(request, f'{producto.nombre} eliminado del carrito.')
    return redirect('ver_carrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('ver_carrito')

def ver_carrito(request):
    return render(request, 'tienda/carrito.html')

# 3. Vista de Confirmación de Compra (Requiere Login)
@login_required(login_url='login')
def confirmar_compra(request):
    carrito = Carrito(request)
    
    # Validación: No comprar si el carrito está vacío
    if not carrito.carrito:
        messages.error(request, "Tu carrito está vacío, agrega productos primero.")
        return redirect('catalogo')
    
    # Generar la Orden
    orden = Orden.objects.create(
        usuario=request.user, 
        total=carrito.obtener_total()
    )
    
    # Generar los detalles de la orden basados en la sesión
    for key, item in carrito.carrito.items():
        producto = Producto.objects.get(id=item['producto_id'])
        DetalleOrden.objects.create(
            orden=orden,
            producto=producto,
            cantidad=item['cantidad'],
            precio_historico=item['precio']
        )
    
    # Limpiar carrito tras la compra y notificar
    carrito.limpiar()
    messages.success(request, "¡Compra confirmada exitosamente! Gracias por tu pedido.")
    return redirect('catalogo')