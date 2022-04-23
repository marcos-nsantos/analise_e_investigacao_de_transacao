from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..validators.csv_validator import validate_csv


class Arquivo(models.Model):
    arquivo = models.FileField(_('Arquivo'), upload_to='csv_files/', validators=[validate_csv])
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    def __str__(self):
        return self.arquivo.name

    class Meta:
        verbose_name = _('Arquivo')
        verbose_name_plural = _('Arquivos')
