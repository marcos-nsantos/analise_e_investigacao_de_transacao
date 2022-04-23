from django import forms
from django.core.exceptions import ValidationError

from ..models.arquivo_model import Arquivo


class FileUploadModelForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['arquivo']
        widgets = {'arquivo': forms.FileInput(attrs={'class': 'file-input'})}
