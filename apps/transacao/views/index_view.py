from django.shortcuts import render, redirect

from ..forms.arquivo_model_form import ArquivoForm


def index(request):
    if request.method == 'POST':
        form = ArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['arquivo']
            print(csv_file.name)
            print(csv_file.size)

            for line in csv_file.readlines():
                print(line)

            form.save()
            return redirect('transacao:index')
    else:
        form = ArquivoForm()
    return render(request, 'transacao/index.html', {'form': form})
