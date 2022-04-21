from csv import reader
from datetime import datetime


def capture_first_date_time_from_csv_file(arquivo_csv):
    for row in reader(arquivo_csv.splitlines(), delimiter=','):
        try:
            data_hora = datetime.strptime(row[7], '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            continue
        return data_hora
