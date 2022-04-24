from datetime import datetime
from csv import reader

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.views import View

from ..forms.file_form import FileUploadModelForm
from ..models.transacao_model import Transacao
from ..util.capture_first_csv_date import capture_first_date_time_from_csv_file


class TransacaoView(LoginRequiredMixin, View):
    form_class = FileUploadModelForm
    template_name = 'transacao/index.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'transacoes': Transacao.objects.all()})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['arquivo'].read().decode('utf-8')
            datetime_fist_line = capture_first_date_time_from_csv_file(csv_file)

            instance = form.save(commit=False)
            instance.save()

            transacoes = []
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

                transacao = Transacao(user=request.user, banco_origem=banco_origem, arquivo=instance,
                                      agencia_origem=agencia_origem, conta_origem=conta_origem,
                                      banco_destino=banco_destino, agencia_destino=agencia_destino,
                                      conta_destino=conta_destino, valor=valor, data_hora=data_hora,
                                      data=data_hora.date())
                transacoes.append(transacao)

            if transacoes:
                try:
                    Transacao.objects.bulk_create(transacoes)
                    messages.success(request, f'{len(transacoes)} transações foram importadas com sucesso.')
                except IntegrityError as e:
                    messages.error(request, f'Não foi possível importar uma ou mais transações. Verifique se o '
                                            f'arquivo possui transações duplicadas ou se já existem transações '
                                            f'importadas.')

        return render(request, self.template_name, {'form': form, 'transacoes': Transacao.objects.all()})
