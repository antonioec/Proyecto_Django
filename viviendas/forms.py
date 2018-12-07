from django import forms


class BusquedaForm(forms.Form):
    OPERACION_CHOICES = (
                          ('Venta', 'Venta'),
                          ('Alquiler', 'Alquiler'),
                          ('', 'Cualquiera')
                        )

    CIUDAD_CHOICES = (
                          ('Arroyo de la Miel', 'Arroyo de la Miel'),
                          ('Benalmadena Pueblo', 'Benalmadena Pueblo'),
                          ('Benalmadena Costa', 'Benalmadena Costa'),
                          ('Torremolinos', 'Torremolinos'),
                          ('Fuengirola', 'Fuengirola'),
                          ('Mijas Costa', 'Mijas Costa'),
                          ('Marbella', 'Marbella'),
                          ('Malaga', 'Malaga'),
                          ('', 'Cualquiera')
                        )

    TIPO_CHOICES = (
                      ('Piso', 'Piso'),
                      ('Piso Atico', 'Piso Atico'),
                      ('Atico Duplex', 'Atico Duplex'),
                      ('Parcela', 'Parcela'),
                      ('Parcela unifamiliar independiente', 'Parcela unifamiliar independiente'),
                      ('Local Comercial', 'Local Comercial'),
                      ('Edificio', 'Edificio'),
                      ('Chalet Adosado', 'Chalet Adosado'),
                      ('Chalet Pareado', 'Chalet Pareado'),
                      ('Chalet Independiente', 'Chalet Independiente'),
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
    ciudad = forms.ChoiceField(choices=CIUDAD_CHOICES, label="ciudad", required=False, widget=forms.Select(
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