from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_coches, name='listar_coches'),
    path('coche/<int:coche_id>/', views.ver_coche, name='ver_coche'),
    path('buscar/', views.buscar_coches, name='buscar_coches'),
   
]

