from datetime import datetime
from csv import reader

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.views import View

from ..forms.file_form import FileUploadForm
from ..models.transacao_model import Transacao
from ..util.capture_first_csv_date import capture_first_date_time_from_csv_file


class TransacaoView(LoginRequiredMixin, View):
    form_class = FileUploadForm
    template_name = 'transacao/index.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'transacoes': Transacao.objects.all()})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file'].read().decode('utf-8')
            datetime_fist_line = capture_first_date_time_from_csv_file(csv_file)

            error_messages = []
            for row in reader(csv_file.splitlines(), delimiter=','):
                banco_origem = row[0]
                agencia_origem = row[1]
                conta_origem = row[2]
                banco_destino = row[3]
                agencia_destino = row[4]
                conta_destino = row[5]

                if "" in row:
                    continue

                try:
                    valor = float(row[6])
                    data_hora = datetime.strptime(row[7], '%Y-%m-%dT%H:%M:%S')
                except ValueError:
                    continue

                if data_hora.date() != datetime_fist_line.date():
                    continue

                try:
                    Transacao.objects.create(banco_origem=banco_origem,
                                             agencia_origem=agencia_origem, conta_origem=conta_origem,
                                             banco_destino=banco_destino, agencia_destino=agencia_destino,
                                             conta_destino=conta_destino, valor=valor, data_hora=data_hora,
                                             data=data_hora.date())
                except IntegrityError as e:
                    if 'Duplicate entry' in str(e):
                        error_messages.append(f'A transação do banco de origem {banco_origem}, agência '
                                              f'{agencia_origem}, conta {conta_origem} para o banco de '
                                              f'destino {banco_destino}, agência {agencia_destino}, conta '
                                              f'{conta_destino} já foi inserida com a data {data_hora.date()}.')

            if error_messages:
                for error_message in error_messages:
                    messages.error(request, error_message)

        return render(request, self.template_name, {'form': form, 'transacoes': Transacao.objects.all()})
