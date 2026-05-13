import random

requisicoes = {

    "login": [
        {
            "metodo": "POST",
            "endpoint": "/api/auth/login",
            "status_code": random.choice([200, 500, 501, 502, 503, 504, 505]),
            "latencia_ms": random.choice([120, 800, 1200, 2500, 4000])
        },
        {
            "metodo": "POST",
            "endpoint": "/api/auth/logout",
            "status_code": random.choice([200, 500, 503, 504]),
            "latencia_ms": random.choice([80, 600, 1800, 3200])
        },
        {
            "metodo": "POST",
            "endpoint": "/api/auth/refresh-token",
            "status_code": random.choice([200, 500, 502, 504]),
            "latencia_ms": random.choice([60, 500, 2000, 3500])
        },
        {
            "metodo": "POST",
            "endpoint": "/api/auth/2fa/verify",
            "status_code": random.choice([200, 401, 500, 503]),
            "latencia_ms": random.choice([150, 900, 2200])
        }
    ],

    "mercado": [
        {
            "metodo": "GET",
            "endpoint": "/api/quotes/PETR4",
            "status_code": random.choice([200, 500, 502, 504]),
            "latencia_ms": random.choice([35, 400, 1400, 3000])
        },
        {
            "metodo": "GET",
            "endpoint": "/api/quotes/VALE3",
            "status_code": random.choice([200, 500, 503]),
            "latencia_ms": random.choice([32, 350, 2500])
        },
        {
            "metodo": "GET",
            "endpoint": "/api/market/orderbook/PETR4",
            "status_code": random.choice([200, 500, 502, 503, 504, 505]),
            "latencia_ms": random.choice([90, 1200, 3200, 5000])
        },
        {
            "metodo": "GET",
            "endpoint": "/api/market/news",
            "status_code": random.choice([200, 500, 503]),
            "latencia_ms": random.choice([90, 700, 2100])
        }
    ],

    "carteira": [
        {
            "metodo": "GET",
            "endpoint": "/api/portfolio",
            "status_code": random.choice([200, 500, 503, 504]),
            "latencia_ms": random.choice([50, 600, 1900, 3400])
        },
        {
            "metodo": "GET",
            "endpoint": "/api/portfolio/performance",
            "status_code": random.choice([200, 500, 504]),
            "latencia_ms": random.choice([70, 850, 2800])
        }
    ],

    "financeiro": [
        {
            "metodo": "GET",
            "endpoint": "/api/account/balance",
            "status_code": random.choice([200, 500, 503]),
            "latencia_ms": random.choice([45, 500, 2300])
        },
        {
            "metodo": "POST",
            "endpoint": "/api/deposits",
            "status_code": random.choice([201, 500, 502, 504]),
            "latencia_ms": random.choice([180, 1200, 2600, 4200])
        }
    ],

    "orders": [
        {
            "metodo": "POST",
            "endpoint": "/api/orders/buy",
            "status_code": random.choice([201, 500, 502, 503, 504]),
            "latencia_ms": random.choice([210, 1300, 2800, 4500])
        },
        {
            "metodo": "POST",
            "endpoint": "/api/orders/sell",
            "status_code": random.choice([201, 500, 501, 503, 504, 505]),
            "latencia_ms": random.choice([250, 1600, 3200, 5000])
        },
        {
            "metodo": "DELETE",
            "endpoint": "/api/orders/cancel",
            "status_code": random.choice([200, 500, 503, 504]),
            "latencia_ms": random.choice([160, 1000, 2600])
        }
    ],

    "trades": [
        {
            "metodo": "GET",
            "endpoint": "/api/trades",
            "status_code": random.choice([200, 500, 503]),
            "latencia_ms": random.choice([95, 700, 2400])
        },
        {
            "metodo": "GET",
            "endpoint": "/api/trades/summary",
            "status_code": random.choice([200, 500, 502, 504]),
            "latencia_ms": random.choice([110, 950, 3100])
        }
    ],

    "validacao_ordens": [
        {
            "metodo": "POST",
            "endpoint": "/api/order-preview",
            "status_code": random.choice([200, 422, 500, 503]),
            "latencia_ms": random.choice([140, 800, 2200])
        },
        {
            "metodo": "POST",
            "endpoint": "/api/orders/validate",
            "status_code": random.choice([200, 422, 500, 504]),
            "latencia_ms": random.choice([170, 1200, 3000])
        }
    ],

    "risk_check": [
        {
            "metodo": "POST",
            "endpoint": "/api/risk/check",
            "status_code": random.choice([200, 500, 503, 504]),
            "latencia_ms": random.choice([130, 700, 2600, 4100])
        }
    ],

    "b3": [
        {
            "metodo": "POST",
            "endpoint": "/api/b3/orders",
            "status_code": random.choice([200, 500, 501, 502, 503, 504, 505]),
            "latencia_ms": random.choice([400, 1800, 3500, 6000])
        },
        {
            "metodo": "GET",
            "endpoint": "/api/b3/session-status",
            "status_code": random.choice([200, 500, 503, 504]),
            "latencia_ms": random.choice([85, 600, 2400])
        }
    ]
}

lista_requisicoes_feitas = []

def GerarRequisicao():

    for i in range(41):

        categoria = random.choice(list(requisicoes.keys()))
        requisicao = random.choice(requisicoes[categoria])

        lista_requisicoes_feitas.append(requisicao)

    return lista_requisicoes_feitas