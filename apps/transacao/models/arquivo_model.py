from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..validators.csv_file import is_csv_file, is_file_empty


class Arquivo(models.Model):
    arquivo = models.FileField(_('Arquivo'), upload_to='arquivos_csv/', null=True, blank=True, validators=[is_csv_file,
                                                                                                           is_file_empty])
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Arquivo')
        verbose_name_plural = _('Arquivos')
        ordering = ['-created_at']

    def __str__(self):
        return self.arquivo.name