from django import forms

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
