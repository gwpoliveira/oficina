from django import forms

class LoginForm(forms.Form):
    usuario = forms.ChoiceField(label='Nome de usuário', required=True )
    senha = forms.ChoiceField(label='Senha', required=True, widget=forms.PasswordInput())