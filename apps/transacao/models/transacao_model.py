from django.db import models
from django.utils.translation import ugettext_lazy as _


class Transacao(models.Model):
    banco_origem = models.CharField(_('Banco origem'), max_length=30, null=False, blank=False)
    agencia_origem = models.CharField(_('Agência origem'), max_length=10, null=False, blank=False)
    conta_origem = models.CharField(_('Conta origem'), max_length=20, null=False, blank=False)
    banco_destino = models.CharField(_('Banco destino'), max_length=30, null=False, blank=False)
    agencia_destino = models.CharField(_('Agência destino'), max_length=10, null=False, blank=False)
    conta_destino = models.CharField(_('Conta destino'), max_length=20, null=False, blank=False)
    valor = models.DecimalField(_('Valor'), max_digits=10, decimal_places=2, null=False, blank=False)
    data_hora = models.DateTimeField(_('Data e hora'), null=False, blank=False)
    data = models.DateField(_('Data'), null=False, blank=False)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Transação')
        verbose_name_plural = _('Transações')
        ordering = ['data_hora']
        constraints = [
            models.UniqueConstraint(
                fields=['banco_origem', 'agencia_origem', 'conta_origem', 'banco_destino', 'agencia_destino',
                        'conta_destino', 'data'], name='unique_transacao')
        ]
