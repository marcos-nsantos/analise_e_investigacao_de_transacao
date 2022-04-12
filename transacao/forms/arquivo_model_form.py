from django import forms

from ..models.arquivo_model import Arquivo


class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['arquivo']
        widgets = {
            'arquivo': forms.FileInput(attrs={'class': 'file-input'})
        }
