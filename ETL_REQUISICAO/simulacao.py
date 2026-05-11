import csv
import random
from datetime import datetime

requisicoes = {

    "login": [
        {
            "metodo": "POST",
            "endpoint": "/api/auth/login",
            "status_code": 200,
            "latencia_ms": 120
        },
        {
            "metodo": "POST",
            "endpoint": "/api/auth/logout",
            "status_code": 200,
            "latencia_ms": 80
        },
        {
            "metodo": "POST",
            "endpoint": "/api/auth/refresh-token",
            "status_code": 200,
            "latencia_ms": 60
        },
        {
            "metodo": "POST",
            "endpoint": "/api/auth/2fa/verify",
            "status_code": 401,
            "latencia_ms": 150
        }
    ],

    "mercado": [
        {
            "metodo": "GET",
            "endpoint": "/api/quotes/PETR4",
            "status_code": 200,
            "latencia_ms": 35
        },
        {
            "metodo": "GET",
            "endpoint": "/api/quotes/VALE3",
            "status_code": 200,
            "latencia_ms": 32
        },
        {
            "metodo": "GET",
            "endpoint": "/api/market/orderbook/PETR4",
            "status_code": 504,
            "latencia_ms": 3200
        },
        {
            "metodo": "GET",
            "endpoint": "/api/market/news",
            "status_code": 200,
            "latencia_ms": 90
        }
    ],

    "carteira": [
        {
            "metodo": "GET",
            "endpoint": "/api/portfolio",
            "status_code": 200,
            "latencia_ms": 50
        },
        {
            "metodo": "GET",
            "endpoint": "/api/portfolio/performance",
            "status_code": 200,
            "latencia_ms": 70
        }
    ],

    "financeiro": [
        {
            "metodo": "GET",
            "endpoint": "/api/account/balance",
            "status_code": 200,
            "latencia_ms": 45
        },
        {
            "metodo": "POST",
            "endpoint": "/api/deposits",
            "status_code": 201,
            "latencia_ms": 180
        }
    ],

    "orders": [
        {
            "metodo": "POST",
            "endpoint": "/api/orders/buy",
            "status_code": 201,
            "latencia_ms": 210
        },
        {
            "metodo": "POST",
            "endpoint": "/api/orders/sell",
            "status_code": 503,
            "latencia_ms": 2800
        },
        {
            "metodo": "DELETE",
            "endpoint": "/api/orders/cancel",
            "status_code": 200,
            "latencia_ms": 160
        }
    ],

    "trades": [
        {
            "metodo": "GET",
            "endpoint": "/api/trades",
            "status_code": 200,
            "latencia_ms": 95
        },
        {
            "metodo": "GET",
            "endpoint": "/api/trades/summary",
            "status_code": 200,
            "latencia_ms": 110
        }
    ],

    "validacao_ordens": [
        {
            "metodo": "POST",
            "endpoint": "/api/order-preview",
            "status_code": 200,
            "latencia_ms": 140
        },
        {
            "metodo": "POST",
            "endpoint": "/api/orders/validate",
            "status_code": 422,
            "latencia_ms": 170
        }
    ],

    "risk_check": [
        {
            "metodo": "POST",
            "endpoint": "/api/risk/check",
            "status_code": 200,
            "latencia_ms": 130
        }
    ],

    "b3": [
        {
            "metodo": "POST",
            "endpoint": "/api/b3/orders",
            "status_code": 504,
            "latencia_ms": 4000
        },
        {
            "metodo": "GET",
            "endpoint": "/api/b3/session-status",
            "status_code": 200,
            "latencia_ms": 85
        }
    ]
}

lista_requisicoes_feitas = []
def GerarRequisicao():
    for i in range(41):
        categoria = random.choice(list(requisicoes.keys()))
        requisicao = random.choice(requisicoes[categoria])
        lista_requisicoes_feitas.append(requisicao)
    return lista_requisicoes_feitas, categoria

resultado, categoria = GerarRequisicao()

ts = datetime.now()

print(ts)

with open('requisicoes.csv', 'w', newline='') as csvfile:
    Cabecalho = ['timestamp', 'metodo', 'endpoint', 'status_code', 'latencia_ms', 'categoria']
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(Cabecalho)

    for requisicao in lista_requisicoes_feitas:
          writer.writerow([ts, requisicao["metodo"], requisicao["endpoint"], requisicao["status_code"], requisicao["latencia_ms"], categoria])