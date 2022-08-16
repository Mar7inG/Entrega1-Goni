from django import forms
from django.contrib.auth.forms import UserCreationForm




class bicisFormulario(forms.Form):

    Codigo = forms.IntegerField()
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Rodado = forms.CharField()
    Color = forms.CharField()
    Descripcion = forms.CharField(max_length=100)
    Precio = forms.IntegerField()
    
   
class repuestosFormulario(forms.Form):
    
    Codigo = forms.IntegerField()
    Tipo = forms.CharField()
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Descripcion = forms.CharField(max_length=100)
    Precio = forms.IntegerField()

class indumentariaFormularios(forms.Form):

    Codigo = forms.IntegerField()
    Tipo = forms.CharField()
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Talle = forms.CharField()
    Descripcion = forms.CharField(max_length=100)
    Precio = forms.IntegerField()

class accesoriosFormulario(forms.Form):
    
    Codigo = forms.IntegerField()
    Tipo = forms.CharField()
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Descripcion = forms.CharField(max_length=100)
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
    edad=forms.IntegerField() 
    Emial=forms.EmailField(max_length=100)
    

class enviarMensaje(forms.Form):

    Nombre=forms.CharField()
    Correo=forms.EmailField()
    Telefono=forms.CharField()
    Mensaje=forms.CharField()

#Formulario para Registrarse
# class registroFormulario(UserCreationForm):

#     # email= forms.EmailField()
#     # password1= forms.CharField(label='Contraseña',widget=forms.PasswordInput)
#     # password2= forms.CharField(label='Repetir la contraseña',widget=forms.PasswordInput)

#     # class Meta:
#     #     model= Use 
    
    

