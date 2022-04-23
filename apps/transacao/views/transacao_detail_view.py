from django.views import View
from django.shortcuts import render

from ..models.transacao_model import Transacao
from ..models.transacao_model import Arquivo


class TransacaoDetailView(View):
    template_file = 'transacao/transacao_detail.html'

    def get(self, request, pk):
        data = Transacao.objects.filter(pk=pk).first()
        transacao = Transacao.objects.filter(arquivo=data.arquivo_id)
        return render(request, self.template_file, {'transacao': transacao, 'data': data})
