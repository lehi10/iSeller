from django import forms
from apps.proveedor.models import Producto



class RegistroProductosForm(forms.ModelForm):
      class Meta:
            model = Producto
            fields =[
            'nombre',
            'medidas',
            'marca',
            'stock',
            'tags',
            'info',
            'precioBasico',
            'descripcion',
            'urlImagen',
		]
            labels = {
		'nombre':       'Nombre del Producto',
            'medidas':      'Medidas y/o Dimensiones',
            'marca':        'Marca',
            'stock':        'Stock actual',
            'tags':         'Tags',
            'info':         'Información',
            'precioBasico': 'Precio Base',
            'descripcion':  'Descripción adicional',
            'urlImagen': 'Seleccione una Imagen',
		}

            widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'medidas':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.TextInput(attrs={'class':'form-control'}),
            'stock':forms.TextInput(attrs={'class':'form-control'}),
            'tags':forms.TextInput(attrs={'class':'form-control'}),
            'info':forms.Textarea(attrs={'class':'form-control','rows': 6, 'maxlength': 480}),
            'precioBasico':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control','rows': 6, 'maxlength': 480}),
		}

