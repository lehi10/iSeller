from django import forms
from django.utils.translation import gettext as _

from apps.proveedor.models import Producto

class ProductoRegistro(forms.ModelForm):

    class Meta:
        model = Producto

        fields = [
            'idProducto',
            'idProveedor',
            'nombre',
            'medidas',
            'marca',
            'stock',
            'calificacion',
            'tags',
            'info',
            'precioBasico',
            'descripcion',
            'urlImagen'
        ]
        labels = {
            'idProducto':'Producto',
            'idProveedor':'Proveedor',
            'nombre':'Nombre',
            'medidas':'Medidas',
            'marca':'Marca',
            'stock':'Stock',
            'calificacion':'Calificacion',
            'tags':'Tags',
            'info':'Info',
            'precioBasico':'PrecioBase',
            'descripcion':'Descripcion',
            'urlImagen':'URL'
        }
        widgets = {
            'idProveedor':forms.ModelChoiceField(queryset = Producto.objects.all()),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'medidas':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.TextInput(attrs={'class':'form-control'}),
            'stock':forms.NumberInput(attrs={'class':'form-control'}),
            'calificacion':forms.NumberInput(attrs={'class':'form-control'}),
            'tags':forms.TextInput(attrs={'class':'form-control'}),
            'info':forms.TextInput(attrs={'class':'form-control'}),
            'precioBasico':forms.NumberInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'urlImagen':forms.URLInput(attrs={'class':'form-control'})
        }
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if not len(nombre)<=100:
            raise forms.ValidationError("El nombre no puede ser mas grande de 100 caracteres")
        return nombre

    def clean_medidas(self):
        medidas = self.cleaned_data.get("medidas")
        if not len(medidas) <=50:
            raise forms.ValidationError("Especifiquelo en menos de 50 caracteres")
        return medidas
    def clean_marca(self):
        marca = self.cleaned_data.get("marca")
        if not len(marca) <=50:
            raise forms.ValidationError("Especifiquelo en menoes de 50 caracteres")
        return marca
    def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock.isdigit() == False:
            raise forms.ValidationError("Introduzca un digito")
        return stock
    def clean_calificacion(self):
        calificacion = self.cleaned_data.get("calificacion")
        if calificacion.isdigit() == False:
            raise forms.ValidationError("Introduzca un digito")
        return calificacion
    def clean_info(self):
        info = self.cleaned_data.get("info")
        if not len(info) <= 500:
            raise forms.ValidationError("Sea mas consiso especifiquelo en menoes de 500 caracteres")
        return info
    def clean_precioBasico(self):
        precioBasico = self.cleaned_data.get("precioBasico")
        if precioBasico.isdigit() == False:
            raise forms.ValidationError("Introduzca un digito")
        return precioBasico
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        if not len(descripcion) <= 500:
            raise forms.ValidationError("Sea mas consiso especifiquelo en menoes de 500 caracteres")
        return descripcion
    def clean_urlImagen(self):
        urlImagen = self.cleaned_data.get("info")
        if not len(urlImagen) <= 1000:
            raise forms.ValidationError("Sea mas consiso especifiquelo en menoes de 500 caracteres")
        return urlImagen
    