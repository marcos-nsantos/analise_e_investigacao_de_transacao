import csv
from datetime import datetime

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

            data_hora = capture_date_time_from_csv_file(csv_file)
            print(f'Date and time from first line of CSV file: {data_hora}')

            form.save()
            return redirect('transacao:index')
    else:
        form = ArquivoForm()
    return render(request, 'transacao/index.html', {'form': form})


def capture_date_time_from_csv_file(arquivo_csv):
    arquivo_csv = arquivo_csv.splitlines()
    data_e_hora = arquivo_csv[0].split(',')[-1]
    return datetime.strptime(data_e_hora, '%Y-%m-%dT%H:%M:%S')

