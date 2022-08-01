from django.contrib import admin
from django.urls import path
from Appventas.views import Formulariobicis, Formularioindumentarias, Formulariorepuestos, inicio, Busquedabicis
from Appventas.views import LeerIndum, LeerBicis, LeerRepu

from Appventas.views import ResultBici
#from Appventas.views import BusquedaIndu, BusquedaRepuesto, RespuestaBuscarIndu, RespuestaBuscarRepuesto
                                  


urlpatterns = [
   
    path('', inicio, name="INICIO"),
    path('FormularioBici/', Formulariobicis, name="bici_formulario"),
    path('repu_formulario/', Formulariorepuestos, name="repu_formulario"),
    path('indu_formulario/', Formularioindumentarias, name="indu_formulario"),
    path('Leerindumentria/', LeerIndum, name="Leerindume"),
    path('LeerBicicletas/', LeerBicis, name="LeerBicis"),
    path('LeerRepuestos/',LeerRepu, name="LeerRepues") ,     

    #en el template. con "direccion"(sin /) entre las comillas, y con "{% url 'name'%}" va el name.         
    path('BusquedaBici/', Busquedabicis, name="Buscar1"),#Ir pagina de busqueda bicis
    path('IrBici/', ResultBici, name="pepe"),#Buscar bici


   # path('buscarRepuesto/', BusquedaRepuesto, name="Buscar2"),#Ir pagina de busqueda repuestos
   # path('busquedaRepuesto/', RespuestaBuscarRepuesto, name="busqueda2"),#Buscar repuesto


    #path('buscarIndumentaria/', BusquedaIndu, name="Buscar3"),#Ir pagina de busqueda indumentaria
    #path('BusquedaIndumentaria/', RespuestaBuscarIndu, name="busqueda2"),#Buscar indumentaria
]