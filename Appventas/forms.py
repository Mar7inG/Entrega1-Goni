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
    Fabricante = forms.CharField()
    Precio = forms.IntegerField()

class indumentariaFormularios(forms.Form):
    Tipo = forms.CharField()
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Talle = forms.CharField()
    Precio = forms.IntegerField()

class enviarMensaje(forms.Form):

    Nombre=forms.CharField()
    Correo=forms.EmailField()
    Telefono=forms.CharField()
    Mensaje=forms.CharField()
    

