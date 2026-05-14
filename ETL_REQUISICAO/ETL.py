import csv
from datetime import datetime
from pathlib import Path
import simulacao
import subprocess
import platform
from datetime import datetime, timedelta
import time
import numpy as np

while True:

    dados = simulacao.GerarRequisicao()
    ping = simulacao.GerarPing()

    ts = datetime.now()

    arquivo_raw = Path('raw.csv')

    if arquivo_raw.is_file():

        with open('raw.csv', 'a', newline='') as csvfile:

            writer = csv.writer(csvfile, delimiter=';')

            for requisicao in dados:

                writer.writerow([
                    ts,
                    requisicao["metodo"],
                    requisicao["endpoint"],
                    requisicao["status_code"],
                    requisicao["latencia_ms"],
                    ping
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

    arquivo_trusted = Path('requisicoes_trusted.csv')

    if arquivo_trusted.is_file():

        with open('requisicoes_trusted.csv', 'a', newline='') as csvfile:

            writer = csv.writer(csvfile, delimiter=';')

            with open('raw.csv', newline='') as rawfile:

                reader = csv.reader(rawfile, delimiter=';', quotechar='|')

                next(reader, None)

                for row in reader:

                    dt = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f")
                    dt_formatado = dt.strftime("%d/%m/%Y %H:%M:%S")

                    metodo = row[1]
                    endpoint = row[2]

                    if "account" in endpoint:
                        categoria = "financeiro"

                    elif "orders" in endpoint:
                        categoria = "ordens"

                    elif "market" in endpoint:
                        categoria = "mercado"

                    elif "b3" in endpoint:
                        categoria = "b3"

                    else:
                        categoria = "trades"

                    status_code = int(row[3])
                    latencia_ms = int(row[4])

                    if status_code < 200 or status_code > 599:
                        tipo_status = 'status code invalido'

                    elif status_code <= 299:
                        tipo_status = 'sucesso'

                    elif status_code <= 499:
                        tipo_status = 'erro_cliente'

                    else:
                        tipo_status = 'erro_servidor'

                    if latencia_ms < 0:
                        nivel_latencia = 'latencia invalida'

                    elif latencia_ms <= 100:
                        nivel_latencia = 'normal'

                    elif latencia_ms <= 500:
                        nivel_latencia = 'moderada'

                    elif latencia_ms <= 2000:
                        nivel_latencia = 'alta'

                    else:
                        nivel_latencia = 'critica'

                    writer.writerow([
                        dt_formatado,
                        metodo,
                        endpoint,
                        status_code,
                        latencia_ms,
                        categoria,
                        tipo_status,
                        nivel_latencia
                    ])

    else:

        with open('requisicoes_trusted.csv', 'a', newline='') as csvfile:

            Cabecalho = [
                'timestamp',
                'metodo',
                'endpoint',
                'status_code',
                'latencia_ms',
                'categoria',
                'tipo_status',
                'nivel_latencia',
                'porcentagem_Volume',
                'p95_latencia',
                'variacao_latencia'
            ]

            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(Cabecalho)

    arquivo_client = Path('requisicoes_Client.csv')

    if arquivo_client.is_file():

        with open('requisicoes_Client.csv', 'a', newline='') as csvfile_client:

            writer = csv.writer(csvfile_client, delimiter=';')

            with open('requisicoes_trusted.csv', 'r', newline='') as csvfile_trusted:

                reader = csv.reader(csvfile_trusted, delimiter=';', quotechar='|')

                next(reader, None)

                contador_requisicao = 0

                contador_atual = 0
                contador_anterior = 0

                agora = datetime.now()

                inicio_atual = agora - timedelta(minutes=15)
                inicio_anterior = agora - timedelta(minutes=30)

                porcentagem = 0

                linhas = []

                latencias = []

                latencias_atuais = []
                latencias_anteriores = []

                for row in reader:

                    latencia_ms = int(row[4])

                    latencias.append(latencia_ms)

                    if not row or row[0] == "timestamp":
                        continue

                    contador_requisicao += 1

                    timestamp = datetime.strptime(row[0], "%d/%m/%Y %H:%M:%S")

                    metodo = row[1]
                    endpoint = row[2]
                    status_code = row[3]
                    latencia_ms = int(row[4])
                    categoria = row[5]
                    tipo_status = row[6]
                    nivel_latencia = row[7]

                    if timestamp >= inicio_atual:
                        contador_atual += 1

                    elif timestamp >= inicio_anterior:
                        contador_anterior += 1

                    linhas.append([
                        timestamp,
                        metodo,
                        endpoint,
                        status_code,
                        latencia_ms,
                        categoria,
                        tipo_status,
                        nivel_latencia
                    ])

                if contador_anterior > 0:

                    porcentagem = (
                        (contador_atual - contador_anterior)
                        / contador_anterior
                    ) * 100

                    round(porcentagem)

                    print(f"{porcentagem:.2f}%")

                if timestamp >= inicio_atual:
                    contador_atual += 1
                    latencias_atuais.append(latencia_ms)

                elif timestamp >= inicio_anterior:
                    contador_anterior += 1
                    latencias_anteriores.append(latencia_ms)

                p95_atual = 0
                p95_anterior = 0
                variacao_p95 = 0

                if len(latencias_atuais) > 0:
                    p95_atual = np.percentile(latencias_atuais, 95)

                if len(latencias_anteriores) > 0:
                    p95_anterior = np.percentile(latencias_anteriores, 95)

                if p95_anterior > 0:
                    variacao_p95 = ((p95_atual - p95_anterior) / p95_anterior) * 100

                round(variacao_p95, 2)

                for linha in linhas:

                    writer.writerow([
                        linha[0],
                        linha[1],
                        linha[2],
                        linha[3],
                        linha[4],
                        linha[5],
                        linha[6],
                        linha[7],
                        porcentagem,
                        p95_atual,
                        variacao_p95
                    ])

    else:

        with open('requisicoes_Client.csv', 'a', newline='') as csvfile_client:

            Cabecalho = [
                'timestamp',
                'metodo',
                'endpoint',
                'status_code',
                'latencia_ms',
                'categoria',
                'tipo_status',
                'nivel_latencia',
                'porcentagem_Volume',
                'p95_latencia',
                'variacao_latencia'
            ]

            writer = csv.writer(csvfile_client, delimiter=';')
            writer.writerow(Cabecalho)

    time.sleep(5)