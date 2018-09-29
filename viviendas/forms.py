from django import forms

class BusquedaForm(forms.Form):
    OPERACION_CHOICES = (
                          ('Venta', 'Venta'),
                          ('Alquiler', 'Alquiler'),
                          ('', 'Cualquiera')
                        )

    UBICACION_CHOICES = (
                          ('Benalmadena Costa', 'Benalmadena Costa'),
                          ('Benalmadena Pueblo', 'Benalmadena Pueblo'),
                          ('Torremolinos', 'Torremolinos'),
                          ('Fuengirola', 'Fuengirola'),
                          ('', 'Cualquiera')
                        )

    TIPO_CHOICES = (
                      ('Apartamento', 'Apartamento'),
                      ('Atico', 'Atico'),
                      ('Adosado', 'Adosado'),
                      ('', 'Cualquiera')
                    )

    identificador = forms.CharField(label="identificador", required=False, widget=forms.TextInput(
        attrs={'class':'form-control',
               'min': 0,
               'placeholder': 'Cualquiera'}
    ))
    operacion = forms.ChoiceField(choices=OPERACION_CHOICES, label="operacion", required=False, widget=forms.Select(
        attrs={'class': 'form-control',
               'placeholder': 'Cualquiera'},
    ))
    dormitorios = forms.IntegerField(label="dormitorios", required=False, widget=forms.NumberInput(
        attrs={'class': 'form-control',
               'min': 1,
               'placeholder': 'Cualquiera'}
    ))
    premin = forms.IntegerField(label="premin", required=False, widget=forms.NumberInput(
        attrs={'class': 'form-control',
               'min': 0,
               'placeholder': 'Cualquiera'}
    ))
    premax = forms.IntegerField(label="premax", required=False, widget=forms.NumberInput(
        attrs={'class': 'form-control',
               'min': 0,
               'placeholder': 'Cualquiera'}
    ))
    ubicacion = forms.ChoiceField(choices=UBICACION_CHOICES, label="ubicacion", required=False, widget=forms.Select(
        attrs={'class': 'form-control',
               'placeholder': 'Cualquiera'}
    ))
    tipo = forms.ChoiceField(choices=TIPO_CHOICES, label="tipo", required=False, widget=forms.Select(
        attrs={'class': 'form-control',
               'placeholder': 'Cualquiera'}
    ))

    banos = forms.IntegerField(label="banos", required=False, widget=forms.NumberInput(
        attrs={'class': 'form-control',
               'min': 1,
               'placeholder': 'Cualquiera'}
    ))
    supmin = forms.IntegerField(label="supmin", required=False, widget=forms.NumberInput(
        attrs={'class': 'form-control',
               'min': 0,
               'placeholder': 'Cualquiera'}
    ))
    supmax = forms.IntegerField(label="supmax", required=False, widget=forms.NumberInput(
        attrs={'class': 'form-control',
               'min': 0,
               'placeholder': 'Cualquiera'}
    ))