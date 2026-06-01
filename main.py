import pandas as pd
import time
import math

# =========================
# CARREGAR DATASET
# =========================

print("Carregando dataset...")

df = pd.read_csv("train_transaction.csv")

# usar parte do dataset para teste inicial
dados = df.head(200000).to_dict(orient="records")

print(f"{len(dados)} transações carregadas.")

# =========================
# FUNÇÃO DE ANÁLISE
# =========================

def analisar_fraude(transacao):

    valor = transacao.get("TransactionAmt", 0)

    resultado = 0

    # simulação de processamento pesado
    for i in range(10000):
        resultado += math.sqrt(valor + i)

    return resultado

# =========================
# PROCESSAMENTO SERIAL
# =========================

print("\nIniciando processamento serial...")

inicio = time.time()

resultados = []

for transacao in dados:
    resultados.append(analisar_fraude(transacao))

fim = time.time()

tempo_serial = fim - inicio

# =========================
# RESULTADO
# =========================

print(f"\nTempo serial: {tempo_serial:.2f} segundos")