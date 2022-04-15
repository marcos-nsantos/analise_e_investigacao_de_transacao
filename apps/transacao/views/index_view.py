import csv
from datetime import datetime

from django.shortcuts import render
from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib import messages

from ..forms.arquivo_model_form import ArquivoForm
from ..models.transacao_model import Transacao


def index(request):
    if request.method == 'POST':
        form = ArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['arquivo'].read().decode('utf-8')
            datetime_fist_line = capture_first_date_time_from_csv_file(csv_file)

            error_messages = []

            with transaction.atomic():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'Arquivo salvo com sucesso!')

                for row in csv.reader(csv_file.splitlines(), delimiter=','):
                    try:
                        banco_origem = row[0]
                        agencia_origem = row[1]
                        conta_origem = row[2]
                        banco_destino = row[3]
                        agencia_destino = row[4]
                        conta_destino = row[5]
                        valor = float(row[6])
                        data_hora = datetime.strptime(row[7], '%Y-%m-%dT%H:%M:%S')

                        if equal_dates(datetime_fist_line, data_hora):
                            continue

                        Transacao.objects.create(arquivo=instance, banco_origem=banco_origem,
                                                 agencia_origem=agencia_origem, conta_origem=conta_origem,
                                                 banco_destino=banco_destino, agencia_destino=agencia_destino,
                                                 conta_destino=conta_destino, valor=valor, data_hora=data_hora)
                    except ValueError:
                        pass
                    except ValidationError as e:
                        error_messages.append(e.message)

            if error_messages:
                for error_message in error_messages:
                    messages.error(request, error_message)
    else:
        form = ArquivoForm()
    return render(request, 'transacao/index.html', {'form': form, 'transacoes': Transacao.objects.all()})


def capture_first_date_time_from_csv_file(arquivo_csv):
    arquivo_csv = arquivo_csv.splitlines()
    data_e_hora = arquivo_csv[0].split(',')[-1]
    return datetime.strptime(data_e_hora, '%Y-%m-%dT%H:%M:%S')


def equal_dates(date1, date2):
    return date1.date() == date2.date()
