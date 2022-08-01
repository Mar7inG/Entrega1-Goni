from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from Appventas.models import bicicletas, repuestos, indumentaria
from Appventas.forms import bicisformulario, repuestosFormulario, indumentariaFormularios

# Create your views here.


def inicio(request):#Template de Inivcio

    return render(request, "inicio.html")


def Save(request):#Template de confirmacion de guardado.

    return render(request, "Save.html")

def Formulariobicis(request):#Template cargar una bici en la tabla

    if request.method == 'POST':
        BiciFormulario=bicisformulario(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",BiciFormulario ) 

        if BiciFormulario.is_valid():
            print("Entro al 2° if")
            data=BiciFormulario.cleaned_data
            #En la tabla que creo con la clase le cargo los datos del formulario de Django
            bici=bicicletas(marca=data['Marca'],modelo=data['Modelo'],rodado=data['Rodado'],color=data['Color'],precio=data['Precio'],)
            bici.save()
            return render(request, "Save.html")
       # else:
        #    return render (request,"inicio2.html")
    else:
        BiciFormulario=bicisformulario()
        return render(request,"biciFormulario.html", {"BiciFormulario": BiciFormulario})


def Formulariorepuestos(request):#Template cargar un repuesto en la tabla

    if request.method == 'POST':
                        #forms.py
        RepuFormulario=repuestosFormulario(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",RepuFormulario ) 

        if RepuFormulario.is_valid():
            print("Entro al 2° if")
            data=RepuFormulario.cleaned_data
            #En la tabla que creo con la clase (models) le cargo los datos del formulario de Django(forms)
                     #models.py   (como se lee esto?: tipo=data['Tipo'])          
            repuesto=repuestos(tipo=data['Tipo'],marca=data['Marca'],modelo=data['Modelo'],fabricante=data['Fabricante'],precio=data['Precio'],)
            repuesto.save()
            return render(request, "Save.html")
        else:
            return render (request,"inicio2.html")
    else:
        RepuFormulario=repuestosFormulario()
        return render(request,"repuestoFormulario.html", {"RepuestosFormularios":RepuFormulario})        

def Formularioindumentarias(request):#Template cargar una indumentaria en la tabla


    if request.method == 'POST':
        InduFormulario=indumentariaFormularios(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",InduFormulario ) 

        if InduFormulario.is_valid():
            print("Entro al 2° if")
            data=InduFormulario.cleaned_data
            #En la tabla que creo con la clase le cargo los datos del formulario de Django
            Indu=indumentaria(tipo=data['Tipo'],marca=data['Marca'],modelo=data['Modelo'],talle=data['Talle'],precio=data['Precio'],)
            Indu.save()
            return render(request, "Save.html")
        else:
            return render (request,"inicio2.html")
    else:
        InduFormulario=indumentariaFormularios()
        return render(request,"indumentariaFormulario.html", {"IndumentariaFormularios": InduFormulario})

#VER FORMULARIOS
def LeerBicis (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioBicicletas=bicicletas.objects.all()
    contexto={"Bicicetas":FormularioBicicletas}
    return render (request, "VerFormulario_Bicicletas.html",contexto)

def LeerRepu (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioRepuestos=repuestos.objects.all()
    contexto={"Repuestos":FormularioRepuestos}
    return render (request, "VerFormulario_Repuestos.html",contexto)



def LeerIndum (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioIndumentaria=indumentaria.objects.all()
    contexto={"Indumentaria":FormularioIndumentaria}
    return render (request, "VerFormulario_Indumentaria.html",contexto)


#BUSQUEDA BICIS

def Busquedabicis(request):

    return render (request, "BusquedaBici.html")

def RespuestaBuscarbicis(request):

    respuesta=f"Estoy buscando la bicicleta modelo: {request.GET['modelo']}"

    return HttpResponse(respuesta)
#BUSQUEDA REPUESTO
def BusquedaRepuesto(request):

    return render (request, "Busquedarepu.html")

def RespuestaBuscarRepuesto(request):

    respuesta=f"Estoy buscando el repuesto de tipo: {request.GET['Tipo']}"

    return HttpResponse(respuesta)
#BUSQUEDA INDUMENTARIA
def BusquedaIndu(request):

    return render (request, "BusquedaIndumentaria.html")

def RespuestaBuscarIndu(request):

    respuesta=f"Estoy buscando la indumentaria de tipo: {request.GET['Tipo']}"

    return HttpResponse(respuesta)



 



