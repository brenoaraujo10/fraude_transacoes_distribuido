import pandas as pd
import time
import math

print("Carregando dataset...")

df = pd.read_csv("train_transaction.csv")

dados = df.head(200000).to_dict(orient="records")

print(f"{len(dados)} transações carregadas.")


def analisar_fraude(transacao):

    valor = transacao.get("TransactionAmt", 0)

    resultado = 0


    for i in range(10000):
        resultado += math.sqrt(valor + i)

    return resultado

print("\nIniciando processamento serial...")

inicio = time.time()

resultados = []

for transacao in dados:
    resultados.append(analisar_fraude(transacao))

fim = time.time()

tempo_serial = fim - inicio

print(f"\nTempo serial: {tempo_serial:.2f} segundos")