from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth import authenticate


class ContactForm(ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-black focus:border-black block w-full p-2.5', 'placeholder': 'Nombre'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Apellido'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': '+56 -'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Correo@mail.com'}))
    motivo = forms.CharField(widget=forms.Textarea(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5' , 'rows': 3, 'placeholder': 'En breves palabras, ¿Por qué nos escribe?'}))
    
    class Meta:
        model = FormularioClientes
        fields = ['nombre', 'apellido', 'telefono', 'correo', 'motivo']


class AccAuthenticationForm(forms.ModelForm):
    username = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control block w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none', 'placeholder': 'Usuario'}))
    password = forms.CharField(required=True, max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control block w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none', 'placeholder': 'Contraseña'}))
    
    class Meta:
        model = Adminsesion
        fields = ('username', 'password')
        
    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Usuario o contraseña incorrectos.')
    
    def __init__(self, *args, **kwargs):
        super(AccAuthenticationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].label = 'Usuario'