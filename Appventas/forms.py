from django import forms




class bicisFormulario(forms.Form):

    Marca = forms.CharField()
    Modelo = forms.CharField()
    Precio = forms.IntegerField()
    Rodado = forms.CharField()
    Color = forms.CharField()
   

class repuestosFormulario(forms.Form):

    Tipo = forms.CharField()
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Precio = forms.IntegerField()

class indumentariaFormularios(forms.Form):
    Tipo = forms.CharField()
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Talle = forms.CharField()
    Precio = forms.IntegerField()

class accesoriosFormulario(forms.Form):

    Tipo = forms.CharField()
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Precio = forms.IntegerField()
class empleadosFormulario(forms.Form):

    Nombre=forms.CharField(max_length=30)
    Apellido=forms.CharField(max_length=30)
    Telefono= forms.IntegerField() 
    Emial=forms.EmailField(max_length=100)
    Cargo=forms.CharField(max_length=30)

class clienteFormulario(forms.Form):

    Nombre=forms.CharField(max_length=30)
    Apellido=forms.CharField(max_length=30)
    Telefono= forms.IntegerField() 
    Emial=forms.EmailField(max_length=100)
    edad=forms.IntegerField() 

class enviarMensaje(forms.Form):

    Nombre=forms.CharField()
    Correo=forms.EmailField()
    Telefono=forms.CharField()
    Mensaje=forms.CharField()

    

