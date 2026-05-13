import csv
from datetime import datetime
from pathlib import Path
import simulacao
import subprocess
import platform

dados = simulacao.GerarRequisicao()

ts = datetime.now()

arquivo = Path('raw.csv')

if arquivo.is_file():

    with open('raw.csv', 'a', newline='') as csvfile:

        writer = csv.writer(csvfile, delimiter=';')

        for requisicao in dados:

            writer.writerow([
                ts,
                requisicao["metodo"],
                requisicao["endpoint"],
                requisicao["status_code"],
                requisicao["latencia_ms"]
            ])

else:

    with open('raw.csv', 'a', newline='') as csvfile:

        Cabecalho = [
            'timestamp',
            'metodo',
            'endpoint',
            'status_code',
            'latencia_ms'
        ]

        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(Cabecalho)

        for requisicao in dados:

            writer.writerow([
                ts,
                requisicao["metodo"],
                requisicao["endpoint"],
                requisicao["status_code"],
                requisicao["latencia_ms"]
            ])

with open('requisicoes_trusted.csv', 'a', newline='') as csvfile:

    Cabecalho = [
        'timestamp',
        'metodo',
        'endpoint',
        'status_code',
        'latencia_ms',
        'categoria',
        'tipo_status',
        'nivel_latencia'
    ]

    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(Cabecalho)

    with open('raw.csv', newline='') as rawfile:

        reader = csv.reader(rawfile, delimiter=';', quotechar='|')

        next(reader, None)

        for row in reader:

            dt = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f").strftime("%d/%m/%Y %H:%M:%S")

            metodo = row[1]
            endpoint = row[2]

            if endpoint.__contains__("account"):
                categoria = "financeiro"

            elif endpoint.__contains__("orders"):
                categoria = "ordens"

            elif endpoint.__contains__("market"):
                categoria = "mercado"

            elif endpoint.__contains__("b3"):
                categoria = "b3"

            else:
                categoria = "trades"

            row[3] = int(row[3])
            row[4] = int(row[4])

            tipo_status = ''

            if row[3] < 200 or row[3] > 599:
                tipo_status = 'status code invalido'

            elif row[3] >= 200 and row[3] <= 299:
                tipo_status = 'sucesso'

            elif row[3] >= 400 and row[3] <= 499:
                tipo_status = 'erro_cliente'

            else:
                tipo_status = 'erro_servidor'

            nivel_latencia = ''

            if row[4] < 0:
                nivel_latencia = 'latencia invalida'

            elif row[4] >= 0 and row[4] <= 100:
                nivel_latencia = 'normal'

            elif row[4] <= 500:
                nivel_latencia = 'moderada'

            elif row[4] <= 2000:
                nivel_latencia = 'alta'

            else:
                nivel_latencia = 'critica'

            status_code = row[3]
            latencia_ms = row[4]

            writer.writerow([
                dt,
                metodo,
                endpoint,
                status_code,
                latencia_ms,
                categoria,
                tipo_status,
                nivel_latencia
            ])

with open('requisicoes_Client.csv', 'a', newline='') as csvfile_client:

    Cabecalho = [
        'timestamp',
        'metodo',
        'endpoint',
        'status_code',
        'latencia_ms',
        'categoria',
        'tipo_status',
        'nivel_latencia'
    ]

    writer = csv.writer(csvfile_client, delimiter=';')
    writer.writerow(Cabecalho)

    with open('requisicoes_trusted.csv', 'r', newline='') as csvfile_trusted:

        reader = csv.reader(csvfile_trusted, delimiter=';', quotechar='|')

        next(reader, None)

        contador_requisicao = 0

        for row in reader:

            contador_requisicao += 1

            timestamp = row[0]
            metodo = row[1]
            endpoint = row[2]
            status_code = row[3]
            latencia_ms = row[4]
            categoria = row[5]
            tipo_status = row[6]
            nivel_latencia = row[7]

            writer.writerow([
                timestamp,
                metodo,
                endpoint,
                status_code,
                latencia_ms,
                categoria,
                tipo_status,
                nivel_latencia
            ])

            
        print("Total de requisições:", contador_requisicao)


