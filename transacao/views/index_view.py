from django.shortcuts import render, redirect

from ..forms.arquivo_model_form import ArquivoForm


def index(request):
    if request.method == 'POST':
        form = ArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['arquivo'].name)
            print(request.FILES['arquivo'].size)
            form.save()
            return redirect('transacao:index')
    else:
        form = ArquivoForm()
    return render(request, 'transacao/index.html', {'form': form})
