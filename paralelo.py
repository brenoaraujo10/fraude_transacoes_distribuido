import pandas as pd
import time
import math
from concurrent.futures import ProcessPoolExecutor


def processar_bloco(bloco):

    resultados = []

    for transacao in bloco:

        valor = transacao.get("TransactionAmt", 0)

        resultado = 0

        for i in range(10000):
            resultado += math.sqrt(valor + i)

        resultados.append(resultado)

    return resultados


def dividir_lista(lista, n):

    tamanho = len(lista) // n

    blocos = []

    for i in range(n):

        inicio = i * tamanho

        if i == n - 1:
            fim = len(lista)
        else:
            fim = (i + 1) * tamanho

        blocos.append(lista[inicio:fim])

    return blocos


if __name__ == "__main__":

    print("Carregando dataset...")

    df = pd.read_csv("train_transaction.csv")

    dados = df.head(200000).to_dict(orient="records")

    print(f"{len(dados)} transações carregadas.")

    for workers in [12]:

        blocos = dividir_lista(dados, workers)

        print(f"\nExecutando com {workers} processos...")

        inicio = time.time()

        with ProcessPoolExecutor(max_workers=workers) as executor:

            resultados = list(
                executor.map(processar_bloco, blocos)
            )

        fim = time.time()

        tempo = fim - inicio

        print(f"{workers} processos -> {tempo:.2f} segundos")