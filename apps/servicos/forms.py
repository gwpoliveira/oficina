from django import forms

from .models import Servico, OrdemServico


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        exclude = ['oficina']

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        exclude = ['oficina']