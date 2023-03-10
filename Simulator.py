import random as random
import numpy as np
import matplotlib.pyplot as plt

# Define as variáveis de estado
fila = 0                        # número de pessoas na fila
servidores_disponiveis = 0
eventos_agendados = []

# Define as funções de eventos
def chegada_cliente(tempo_atual, capacidade_fila, tempo_atendimento_medio, tempo_chegada_medio ):
    global fila
    global servidores_disponiveis
    fila += 1
    if fila <= capacidade_fila:
        if servidores_disponiveis > 0:
            servidores_disponiveis -= 1
            tempo_atendimento = random.expovariate(1/tempo_atendimento_medio) # gera intervalos de tempo para o atendimento
            agendar_evento(conclusao_atendimento, tempo_atual + tempo_atendimento)
    else:
        fila -= 1

    tempo_chegada = random.expovariate(1/tempo_chegada_medio) # gera intervalos de tempo para a chegada de clientes
    agendar_evento(chegada_cliente, tempo_atual + tempo_chegada)

# Define a função para agendar eventos
def agendar_evento(funcao_evento, tempo_evento):
    global eventos_agendados
    eventos_agendados.append((tempo_evento, funcao_evento)) 

def conclusao_atendimento(tempo_atual, tempo_atendimento_medio):
    global fila
    global servidores_disponiveis
    fila -= 1
    if fila >= 0:
        if fila > 0:
            tempo_atendimento = random.expovariate(1/tempo_atendimento_medio) # gera intervalos de tempo para o atendimento
            agendar_evento(conclusao_atendimento, tempo_atual + tempo_atendimento)
        else:
            servidores_disponiveis += 1

# Define a função principal do simulador
def simulador(tempo_simulacao, tempo_chegada_medio, tempo_atendimento_medio, num_servidores):
    global fila
    global servidores_disponiveis
    global eventos_agendados

    # Inicializa as variáveis de estado
    fila = 0
    servidores_disponiveis = num_servidores
    eventos_agendados = []

    # Agenda o primeiro evento
    tempo_chegada = random.expovariate(1/tempo_chegada_medio) # gera intervalos de tempo para a chegada de clientes
    agendar_evento(chegada_cliente, tempo_chegada)

    # Executa a simulação
    tempo_atual = 0
    while tempo_atual < tempo_simulacao:
        if len(eventos_agendados) == 0:
            break
        else:
            tempo_proximo_evento, proximo_evento = eventos_agendados.pop(0)
            tempo_atual = tempo_proximo_evento
            proximo_evento(tempo_atual, tempo_atendimento_medio)

    # Gera os gráficos
    plt.hist(fila, bins=range(0, 20))
    plt.title('Histograma da fila')
    plt.xlabel('Tamanho da fila')
    plt.ylabel('Frequência')
    plt.show()

# Executa o simulador e armazena os resultados
simulador(120, 5, 3, 2)
