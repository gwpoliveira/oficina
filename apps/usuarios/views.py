from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from .forms import LoginForm

# Create your views here.
def login_usuario(request):
    template_name = 'usuarios/login.html'    
    context  = {}
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_date['usuario']
            senha = form.cleaned_date['senha']
            user = authenticate(username=usuario, password=senha)
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponse('<h1> você fez login </h1>')
        else:
            return HttpResponse('<h1> erro no login </h1>')
    return render(request, template_name, context)