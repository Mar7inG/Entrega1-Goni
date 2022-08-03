from django.contrib import admin
from django.urls import path
from Appventas.views import Formulariobicis, Formularioindumentarias, Formulariorepuestos, inicio, Busquedabicis
from Appventas.views import LeerIndum, LeerBicis, LeerRepu

from Appventas.views import ResultBici
from Appventas.views import BusquedaIndu, BusquedaRepues, ResultIndu, ResultRepues
from Appventas.views import Nosotros
from Appventas.views import Formularios
#from Appventas.views import BusquedaIndu, BusquedaRepuesto, RespuestaBuscarIndu, RespuestaBuscarRepuesto
                                  


urlpatterns = [
    
     #Simple acceso
    path('', inicio, name="INICIO"),
    path('Formularios', Formularios ,name="Formularios"),
    path('Nosotros/', Nosotros,name="Nosotros"),
    #CARGAR DATOS
    path('FormularioBici/', Formulariobicis, name="bici_formulario"),
    path('repu_formulario/', Formulariorepuestos, name="repu_formulario"),
    path('indu_formulario/', Formularioindumentarias, name="indu_formulario"),
    #VER FORULARIOS
    path('Leerindumentria/', LeerIndum, name="Leerindume"),
    path('LeerBicicletas/', LeerBicis, name="LeerBicis"),
    path('LeerRepuestos/',LeerRepu, name="LeerRepues") ,     
    #BUSCAR
    #en el template. con "direccion"(sin /) entre las comillas, y con "{% url 'name'%}" va el name.         
    path('BusquedaBici/', Busquedabicis, name="Buscar1"),#Ir pagina de busqueda bicis
    path('IrBici/', ResultBici, name="Busqueda1"),#Buscar bici
    path('BuscarRepuesto/',BusquedaRepues,name="Buscar2"),
    path('IrRepues/',ResultRepues,name="Busqueda2"),
    path('BuscarIndumentaria/',BusquedaIndu, name="Buscar3"),
    path('Irndumentaria/', ResultIndu, name="Busqueda3"),
]

