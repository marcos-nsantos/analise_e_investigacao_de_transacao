from django import forms
from django.core.exceptions import ValidationError


class FileUploadForm(forms.Form):
    file = forms.FileField(label='Arquivo', required=True, widget=forms.FileInput(attrs={'class': 'file-input'}))

    def clean_file(self):
        cleaned_data = super().clean()
        file = cleaned_data.get('file')

        if file.name.split('.')[-1] != 'csv':
            raise ValidationError('O arquivo deve ser do tipo CSV.')

        if file.size > 1048576:
            raise ValidationError('O arquivo deve ter no máximo 10MB.')

        if file.size == 0:
            raise ValidationError('O arquivo não pode estar vazio.')

        return cleaned_data
