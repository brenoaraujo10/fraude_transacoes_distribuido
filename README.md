# Sistema Distribuído de Detecção de Golpes e Fraudes nas Transações

O sistema utiliza o dataset IEEE-CIS Fraud Detection para simular a análise de transações financeiras e detecção de possíveis fraudes em ambiente bancário.

---

## Dataset Utilizado

**IEEE-CIS Fraud Detection**

Tamanho aproximado: 1.35 GB

Fonte: Kaggle

---

## Objetivo

Implementar técnicas de processamento serial e paralelo para analisar grandes volumes de transações financeiras, medindo desempenho e ganho de eficiência.

---

## Tecnologias Utilizadas

- Python
- Pandas

---

## Configuração da Máquina Utilizada

| Item | Descrição |
| --------------------------- | ---------------------------------------- |
| Processador | Intel® Core™ i3-10110U CPU @ 2.10 GHz |
| Número de núcleos | 2 núcleos físicos / 4 threads lógicas |
| Memória RAM | 12 GB DDR4 2667 MHz |
| Sistema Operacional | Windows 11 |
| Linguagem utilizada | Python 3.14 |
| Biblioteca de paralelização | concurrent.futures (ProcessPoolExecutor) |
| Compilador / Versão | Python 3.14 |

---

## Tempo Serial

A princípio foi realizado um benchmark serial utilizando aproximadamente 200 mil transações do dataset.

### Resultados Obtidos

**3 Execuções:**

- 1° - 286,62 segundos
- 2° - 444,04 segundos
- 3° - 396,91 segundos

**Tempo serial médio:** 375,86 segundos

**Aproximadamente:** 6 minutos e 16 segundos

| Execução | Tempo (s) |
| --------------- | ---------: |
| 1ª Execução | 286,62 |
| 2ª Execução | 444,04 |
| 3ª Execução | 396,91 |
| **Tempo Médio** | **375,86** |

---

## Tempo Paralelo

Após a execução serial, foi implementado o processamento paralelo utilizando a biblioteca ProcessPoolExecutor. O objetivo foi distribuir o processamento das transações entre múltiplos processos e comparar o desempenho obtido em diferentes níveis de paralelismo.

| Processos | Tempo (s) |
| --------- | --------: |
| 2 | 338,62 |
| 4 | 190,78 |
| 8 | 180,19 |
| 12 | 183,69 |

<h3 align="center">Gráfico de Tempo de Execução</h3>

<p align="center">
  <img src="graficos/tempo_execucao.jpeg" width="600">
</p>

---

## Speedup

O speedup representa o ganho de desempenho obtido pela execução paralela em comparação com a execução serial.

| Processos | Tempo (s) | Speedup |
| --------- | --------: | ------: |
| 2 | 338,62 | 1,11 |
| 4 | 190,78 | 1,97 |
| 8 | 180,19 | 2,09 |
| 12 | 183,69 | 2,05 |

<h3 align="center">Gráfico de Speedup</h3>

<p align="center">
  <img src="graficos/speedup.jpeg" width="600">
</p>

---

## Eficiência

A eficiência indica o nível de aproveitamento dos processos utilizados durante a execução paralela. Esse indicador permite avaliar o impacto do overhead de gerenciamento à medida que o número de processos aumenta.

| Processos | Speedup | Eficiência (%) |
| --------- | ------: | -------------: |
| 2 | 1,11 | 55,50 |
| 4 | 1,97 | 49,25 |
| 8 | 2,09 | 26,13 |
| 12 | 2,05 | 17,08 |

<h3 align="center">Gráfico de Eficiência</h3>

<p align="center">
  <img src="graficos/eficiencia.jpeg" width="600">
</p>

---

## Conclusão

Os resultados demonstraram que a utilização de processamento paralelo proporcionou ganhos significativos de desempenho na análise das transações financeiras. O melhor resultado foi obtido com 8 processos, reduzindo o tempo de execução de 375,86 segundos para 180,19 segundos.

A utilização de 12 processos apresentou desempenho ligeiramente inferior ao obtido com 8 processos, comportamento esperado devido ao overhead de gerenciamento dos processos e às limitações do hardware utilizado.

---

## Alunos

- Breno Ferreira - 069800
- Yuri Bacelar - 076605