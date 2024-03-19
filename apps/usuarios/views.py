from django.shortcuts import render

# Create your views here.
def login(request):
    template_name = 'usuarios/login.html'    
    context  = {}
    return render(request, template_name, context)