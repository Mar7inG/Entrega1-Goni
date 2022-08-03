from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from Appventas.models import ( 
                    bicicletas, repuestos, indumentaria,EnviarMensajes,
)
from Appventas.forms import (
    bicisformulario, repuestosFormulario, indumentariaFormularios, enviarMensaje
)


# Views de simple acceso
def Nosotros(request):#Template de Nostros

    return render(request, "QuienesSomos.html")

def IrEnviarMensaje(request):#Template de Nostros

    return render(request, "EnviarMensaje.html")

def Formularios(request):#Template de Formularios

    return render(request, "Formularios.html")

def inicio(request):#Template de Inivcio

    return render(request, "inicio.html")

#Enviar Mensaje
def EnviarMensaje(request):
    
    if request.method == 'POST':
            MensajeEnviado=enviarMensaje(request.POST)

            if MensajeEnviado.is_valid():
                data=MensajeEnviado.cleaned_data# si le pongo parentesis o corchetes y entre comillas una variable en particular pide solo esa
                mensaje=EnviarMensajes(nombre=data["Nombre"],correo=["Correo"],telefono=["Telefono"],mensaje=["Mensaje"])
                mensaje.save()
                return render(request,"Save.html")
    else:
        MensajeEnviado=enviarMensaje()
        return render (request,"EnviarMensaje.html",{"MensajeaEnviar":MensajeEnviado})


#Formularios
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
        return render(request,"FormularioBicicletas.html", {"BiciFormulario": BiciFormulario})


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
        return render(request,"FormularioIndumentaria.html", {"IndumentariaFormularios": InduFormulario})


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
        return render(request,"FormularioRepuestos.html", {"RepuestosFormularios":RepuFormulario})        


#VER FORMULARIOS
def LeerBicis (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioBicicletas=bicicletas.objects.all()
    contexto={"Bicicletas":FormularioBicicletas}
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

def ResultBici(request):
    print(request.GET)

    if request.GET["modelo"]: 
        print("Entro al if")
        modelo=request.GET["modelo"]
        print(modelo)
        modelos=bicicletas.objects.filter(modelo__icontains=modelo)
        print(modelos)
        return render (request,"BusquedaBicicleta.html", {"modelos": modelos , "modelo":modelo})
    else:
        print("No entro al if")
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaBicicleta.html")
    

#BUSQUEDA INDUMENTARIA
def BusquedaIndu(request):

    return render (request, "BusquedaIndu.html")

def ResultIndu(request):
    print(request.GET)

    if request.GET["tipo"]: 
        print("Entro al if")
        tipo=request.GET["tipo"]
        print(tipo)
        tipos=indumentaria.objects.filter(tipo__icontains=tipo)
        print(tipos)
        return render (request,"BusquedaIndumentaria.html", {"tipos": tipos ,"tipo":tipo})
    else:
        print("No entro al if")
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaIndumentaria.html")
 

#BUSQUEDA RESPUESTO
def BusquedaRepues(request):

    return render (request, "BusquedaRepu.html")

def ResultRepues(request):
    print(request.GET)

    if request.GET["tipo"]: 
        print("Entro al if")
        tipo=request.GET["tipo"]
        print(tipo)
        tipos=repuestos.objects.filter(tipo__icontains=tipo)
        print(tipos)
        return render (request,"BusquedaRepuesto.html", {"tipos": tipos , "tipo":tipo})
    else:
        print("No entro al if")
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaRepuesto.html")
    

    







 



