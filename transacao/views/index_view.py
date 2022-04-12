from django.shortcuts import render

from ..forms.arquivo_model_form import ArquivoForm


def index(request):
    form = ArquivoForm()
    return render(request, 'transacao/index.html', {'form': form})
