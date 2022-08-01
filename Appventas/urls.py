from django.contrib import admin
from django.urls import path
from Appventas.views import Formulariobicis, Formularioindumentarias, Formulariorepuestos, inicio, Busquedabicis
from Appventas.views import LeerIndum, LeerBicis, LeerRepu
from Appventas.views import RespuestaBuscarbicis
from Appventas.views import BusquedaIndu, BusquedaRepuesto, RespuestaBuscarIndu, RespuestaBuscarRepuesto
                                  


urlpatterns = [
   
    path('', inicio, name="INICIO"),
    path('bici_formulario/', Formulariobicis, name="bici_formulario"),
    path('repu_formulario/', Formulariorepuestos, name="repu_formulario"),
    path('indu_formulario/', Formularioindumentarias, name="indu_formulario"),
    path('Leerindumentria/', LeerIndum, name="Leerindume"),
    path('LeerBicicletas/', LeerBicis, name="LeerBicis"),
    path('LeerRepuestos/',LeerRepu, name="LeerRepues") ,     


    path('BusquedaBici/', Busquedabicis, name="BuscarBicis"),#Ir pagina de busqueda bicis
    path('RespuestaBusquedaBici/', RespuestaBuscarbicis, name="busquedaBicis"),#Buscar bici


    path('buscarRepuesto/', BusquedaRepuesto, name="buscarRepuesto"),#Ir pagina de busqueda repuestos
    path('busquedaRepuesto/', RespuestaBuscarRepuesto, name="busquedaRepuesto"),#Buscar repuesto


    path('buscarIndumentaria/', BusquedaIndu, name="buscarIndumentaria"),#Ir pagina de busqueda indumentaria
    path('BusquedaIndumentaria/', RespuestaBuscarIndu, name="BusquedaIndumentaria"),#Buscar indumentaria
]