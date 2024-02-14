from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import ContactForm, AccAuthenticationForm
from .models import FormularioClientes
from django.contrib import messages

from django.core.paginator import Paginator
# Create your views here.

def HomeView(request):
    return render(request, 'home.html')

def ContactView(request):
    if request.method == 'POST':
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Hemos recibido su mensaje, pronto nos pondremos en contacto con usted.')

    context = {'form': ContactForm}
    return render(request, 'contact.html', context)

def TablaAd(request):
    # Validación para que los usuarios que no estén logeados no puedan acceder a la página
    if not request.user.is_authenticated:
        return redirect('home')

    else:
        # received = FormularioClientes.objects.all().order_by('-id')

        paginator = Paginator(FormularioClientes.objects.all(), 3)
        page = request.GET.get('page')
        received = paginator.get_page(page)

        context = {'received': received}
    
    return render(request, 'adminTable/table_received.html', context)

def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('home')
    
    else:
        event = FormularioClientes.objects.get(id=id)
        if event is not None:
            event.delete()
            messages.success(request, 'Se ha eliminado correctamente')
            return redirect('recepted')
        else:
            messages.error(request, 'Ese registro ya fue eliminado')
            return redirect('recepted')


def login_user(request):
    data = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AccAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                auth_login(request, user)
                return redirect('recepted')
    
    else:
        form = AccAuthenticationForm()
    
    data['form'] = form

    return render(request, 'registration/login.html', data)