from django.urls import path
from . import  views


urlpatterns = [
    path('', views.index, name='index'),
     path('carrito/', views.Carrito, name='Carrito'),
    path('ciberSeguridad/', views.ciberseguridad, name='ciberseguridad'),
    path('IA/', views.IA, name='IA'),
    path('misionVision/', views.MisionVision, name='MisionVision'),
    path('noticiasDuoc/', views.noticiasDuoc, name='noticiasDuoc'),
    path('pagos/', views.pago2, name='pago'),
   
]