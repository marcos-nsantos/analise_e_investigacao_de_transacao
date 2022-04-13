from django.db import models
from django.utils.translation import ugettext_lazy as _

from .arquivo_model import Arquivo


class Transacao(models.Model):
    arquivo = models.ForeignKey(Arquivo, on_delete=models.CASCADE, verbose_name=_('Arquivo'))
    banco_origem = models.CharField(_('Banco origem'), max_length=30, null=False, blank=False)
    agencia_origem = models.CharField(_('Agência origem'), max_length=10, null=False, blank=False)
    conta_origem = models.CharField(_('Conta origem'), max_length=20, null=False, blank=False)
    banco_destino = models.CharField(_('Banco destino'), max_length=30, null=False, blank=False)
    agencia_destino = models.CharField(_('Agência destino'), max_length=10, null=False, blank=False)
    conta_destino = models.CharField(_('Conta destino'), max_length=20, null=False, blank=False)
    valor = models.DecimalField(_('Valor'), max_digits=10, decimal_places=2, null=False, blank=False)
    data_hora = models.DateTimeField(_('Data e hora'), null=False, blank=False)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Transação')
        verbose_name_plural = _('Transações')
        ordering = ['data_hora']

    def __str__(self):
        return f'{self.conta_origem} - {self.conta_destino} - {self.valor}'
