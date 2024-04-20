from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ServicoForm, OrdemServicoForm

from .models import Servico, OrdemServico
from geral.models import Oficina


@login_required
def lista_servicos(request):
    template_name = 'servicos/lista_servicos.html'
    oficina = Oficina.objects.filter(usuario=request.user).first()
    servicos = Servico.objects.filter(oficina=oficina)
    context = {
        'servicos': servicos,
    }
    return render(request, template_name, context)


@login_required
def novo_servico(request):
    template_name = 'servicos/novo_servico.html'
    context = {}
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        oficina = Oficina.objects.filter(usuario=request.user).first()
        if form.is_valid():
            sf = form.save(commit=False)
            sf.oficina = oficina
            sf.save()
            messages.success(request, 'Servico adicionado com sucesso')
            return redirect('servicos:lista_servicos')
    form = ServicoForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def editar_servico(request, pk):
    template_name = 'servicos/novo_servico.html'
    context = {}
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(data=request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço atualizado com sucesso')
            return redirect('servicos:lista_servicos')  # Corrected URL name
    else:
        form = ServicoForm(instance=servico)
    context['form'] = form
    return render(request, template_name, context)


# ***************************************** Ordem de Serviços *****************************************
@login_required
def criar_ordem_servico(request):
    template_name = 'servicos/criar_ordem_servico.html'
    context = {}
    oficina = get_object_or_404(Oficina, usuario=request.user)
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            osf = form.save(commit=False)
            osf.oficina = oficina
            osf.save()
            messages.success(request, 'Ordem cadastrado com sucesso')
            return redirect('servicos:lista_ordem_servico')
    form = OrdemServicoForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def lista_ordem_servico(request):
    template_name = 'servicos/lista_ordem_servico.html'
    oficina = get_object_or_404(Oficina, usuario=request.user)
    ordens_servicos = OrdemServico.objects.filter(oficina=oficina)
    context = {
        'ordens_servicos': ordens_servicos
    }
    return render(request, template_name, context)


@login_required
def editar_ordem_servico(request, pk):
    template_name = 'servicos/criar_ordem_servico.html'
    context = {}
    ordem_servico = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        form = OrdemServicoForm(data=request.POST, instance=ordem_servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ordem de servico atualizado com sucesso!')
            return redirect('servicos:lista_ordem_servico')  # Corrected URL name
    else:
        form = OrdemServicoForm(instance=ordem_servico)
    context['form'] = form
    return render(request, template_name, context)
