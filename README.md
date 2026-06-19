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
| Processador | ...|
| Número de núcleos | .... |
| Memória RAM | .... |
| Sistema Operacional | ... |
| Linguagem utilizada | ... |
| Biblioteca de paralelização | concurrent.futures (ProcessPoolExecutor) |
| Compilador / Versão | Python 3.14 |

---

## Tempo Serial

A princípio foi realizado um benchmark serial utilizando aproximadamente 200 mil transações do dataset.

### Resultado Obtido

Tempo serial : 

| Execução | Tempo (s) |
| --------------- | ---------: |
| Execução | 107,21 |


---

## Tempo Paralelo

Após a execução serial, foi implementado o processamento paralelo utilizando a biblioteca ProcessPoolExecutor. O objetivo foi distribuir o processamento das transações entre múltiplos processos e comparar o desempenho obtido em diferentes níveis de paralelismo.

| Processos | Tempo de Execução (s) |
| --------- | --------------------: |
| 2         |                 67,23 |
| 4         |                 35,42 |
| 8         |                 24,32 |
| 12        |                 22,29 |

<p align="center">
  <img src="graficos/tempo_execucao.png" width="600">
</p>

---

## Speedup

O speedup representa o ganho de desempenho obtido pela execução paralela em comparação com a execução serial.

| Processos | Tempo (s) | Speedup |
| --------- | --------: | ------: |
| 2         |     67,23 |    1,59 |
| 4         |     35,42 |    3,03 |
| 8         |     24,32 |    4,41 |
| 12        |     22,29 |    4,81 |


<p align="center">
  <img src="graficos/speedup.png" width="600">
</p>


---

## Eficiência

A eficiência indica o nível de aproveitamento dos processos utilizados durante a execução paralela. Esse indicador permite avaliar o impacto do overhead de gerenciamento à medida que o número de processos aumenta.

| Processos | Speedup | Eficiência (%) |
| --------- | ------: | -------------: |
| 2         |    1,59 |          79,73 |
| 4         |    3,03 |          75,67 |
| 8         |    4,41 |          55,10 |
| 12        |    4,81 |          40,08 |


<p align="center">
  <img src="graficos/eficiencia.png" width="600">
</p>

---

## Conclusão

Os resultados demonstraram que a utilização de processamento paralelo proporcionou ganhos significativos de desempenho na análise das transações financeiras. 

---

## Alunos

- Breno Ferreira - 069800
- Yuri Bacelar - 076605