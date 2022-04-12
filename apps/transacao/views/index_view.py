import csv

from django.shortcuts import render, redirect

from ..forms.arquivo_model_form import ArquivoForm


def index(request):
    if request.method == 'POST':
        form = ArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['arquivo'].name)
            print(request.FILES['arquivo'].size)

            csv_file = request.FILES['arquivo'].read().decode('utf-8')
            for row in csv.reader(csv_file.splitlines(), delimiter=','):
                print(row)

            form.save()
            return redirect('transacao:index')
    else:
        form = ArquivoForm()
    return render(request, 'transacao/index.html', {'form': form})
