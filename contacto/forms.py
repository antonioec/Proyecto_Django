from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=False, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'id': 'txtNombre',
               'novalidate': '',
               'placeholder': 'Introduzca su nombre'}
    ))
    email = forms.EmailField(label="Email", required=False, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'id': 'txtEmail',
               'novalidate':'',
               'placeholder': 'Introduzca su correo electronico'}
    ))
    content = forms.CharField(label="Contenido", required=False, widget=forms.Textarea(
        attrs={'class': 'form-control',
               'id': 'txtArea',
               'novalidate': '',
               'rows': 5,
               'cols': 30,
               'placeholder': 'Introduzca su mensaje'}
    ))
