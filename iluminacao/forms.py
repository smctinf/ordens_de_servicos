from django import forms
from django.forms import ModelForm, ValidationError
from .models import OrdemDeServico


class OS_Form(ModelForm):    
    
    class Meta:
        model = OrdemDeServico
        widgets = {                
            'cpf': forms.TextInput(attrs={'onkeydown':'mascara(this, icpf)'}),
            'telefone': forms.TextInput(attrs={'onkeydown':'mascara(this, itel)'})
        }
        exclude = ['numero', 'dt_inclusao', 'atendente', 'dt_conclusao']