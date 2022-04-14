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
            data_hora_primeira_linha = capture_date_time_from_csv_file(csv_file)

            error_messages = []
            try:
                with transaction.atomic():
                    instance = form.save(commit=False)
                    instance.save()

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

                            if data_hora_primeira_linha.date() == data_hora.date() and not transaction_already_exists(
                                    banco_origem, agencia_origem, conta_origem, banco_destino, agencia_destino,
                                    conta_destino, data_hora, valor):
                                transacao = Transacao(arquivo=instance, data_hora=data_hora_primeira_linha,
                                                      banco_origem=banco_origem,
                                                      agencia_origem=agencia_origem, conta_origem=conta_origem,
                                                      banco_destino=banco_destino, agencia_destino=agencia_destino,
                                                      conta_destino=conta_destino, valor=valor)
                                transacao.full_clean()
                                transacao.save()
                            elif transaction_already_exists(banco_origem, agencia_origem, conta_origem, banco_destino,
                                                            agencia_destino, conta_destino, data_hora, valor):
                                error_messages.append(f'Não foi possível salvar a transação {row}. Pois esta já existe '
                                                      f'em nossa base de dados.')
                        except ValueError:
                            pass
                        except ValidationError:
                            pass
            except Exception as e:
                print(e)
            else:
                messages.success(request, 'Arquivo importado com sucesso!')

            if error_messages:
                for error_message in error_messages:
                    messages.error(request, error_message)

    else:
        form = ArquivoForm()
    return render(request, 'transacao/index.html', {'form': form})


def capture_date_time_from_csv_file(arquivo_csv):
    arquivo_csv = arquivo_csv.splitlines()
    data_e_hora = arquivo_csv[0].split(',')[-1]
    return datetime.strptime(data_e_hora, '%Y-%m-%dT%H:%M:%S')


def transaction_already_exists(banco_origem, agencia_origem, conta_origem, banco_destino, agencia_destino,
                               conta_destino, data_hora, valor):
    is_transaction = Transacao.objects.filter(banco_origem=banco_origem, agencia_origem=agencia_origem,
                                              conta_origem=conta_origem,
                                              banco_destino=banco_destino, agencia_destino=agencia_destino,
                                              conta_destino=conta_destino, data_hora__year=data_hora.year,
                                              data_hora__month=data_hora.month, data_hora__day=data_hora.day,
                                              valor=valor).exists()
    return is_transaction
