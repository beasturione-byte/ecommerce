from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),
    path('limpiar/', views.limpiar_carrito, name='limpiar'),
    path('confirmar/', views.confirmar_compra, name='confirmar_compra'),
]