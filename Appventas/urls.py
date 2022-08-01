from django.contrib import admin
from django.urls import path
from Appventas.views import Formulariobicis, Formularioindumentarias, Formulariorepuestos, inicio, Buscquedabicis
from Appventas.views import LeerIndum, LeerBicis, LeerRepu
                                  


urlpatterns = [
   
    path('', inicio, name="INICIO"),
    path('bici_formulario/', Formulariobicis, name="bici_formulario"),
    path('repu_formulario/', Formulariorepuestos, name="repu_formulario"),
    path('indu_formulario/', Formularioindumentarias, name="indu_formulario"),
    path('busquedaBicis/', Buscquedabicis, name="BusquedaBicis"),
    path('buscarBicis/', Buscquedabicis, name="BusquedaBicis"),
    path('Leerindumentria/', LeerIndum, name="Leerindume"),
    path('LeerBicicletas/', LeerBicis, name="LeerBicis"),
    path('LeerRepuestos/',LeerRepu, name="LeerRepues") ,     
]