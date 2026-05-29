dados_missao =[
[40, 25, 15, 75, 35],
[42, 22, 12, 73, 30],
[41, 20, 10, 71, 28],
[43, 18, 8, 70, 25],
[44, 15, 6, 68, 22],
[45, 12, 5, 65, 20]
]


areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

total_temperatura  = 0
total_comunicacao  = 0
total_bateria      = 0
total_oxigenio     = 0
total_estabilidade = 0
riscos             = []
pontuacoes_area    = [0, 0, 0, 0, 0]

def analisar_temperatura(valor):
    if valor < 18:
        classificacao = "ATENÇÃO"
        msg = "Temperatura baixa"
    elif 18 <= valor <= 30:
        classificacao = "NORMAL"
        msg = "Temperatura estável"
    elif 30 < valor <= 35:
        classificacao = "ATENÇÃO"
        msg = "Temperatura elevada"
    else:
        classificacao = "CRÍTICO"
        msg = "Risco de superaquecimento"
    return classificacao, msg

def analisar_comunicacao(valor):
    if valor < 30:
        classificacao = "CRÍTICO"
        msg = "Comunicação com a base em nível crítico"
    elif 30 <= valor <= 59:
        classificacao = "ATENÇÃO"
        msg = "Comunicação instável"
    else:
        classificacao = "NORMAL"
        msg = "Comunicação estável"
    return classificacao, msg

def analisar_bateria(valor):
    if valor < 20:
        classificacao = "CRÍTICO"
        msg = "Bateria em nível crítico"
    elif 20 <= valor <= 49:
        classificacao = "ATENÇÃO"
        msg = "Bateria abaixo do recomendado"
    else:
        classificacao = "NORMAL"
        msg = "Energia estável"
    return classificacao, msg

def analisar_oxigenio(valor):
    if valor < 80:
        classificacao = "CRÍTICO"
        msg = "Oxigênio em nível crítico"
    elif 80 <= valor <=89:
        classificacao = "ATENÇÃO"
        msg = "Oxigênio abaixo do ideal"
    else:
        classificacao = "NORMAL"
        msg = "Oxigênio adequado"
    return classificacao, msg

def analisar_estabilidade(valor):
    if valor < 40:
        classificacao = "CRÍTICO"
        msg = "Estabilidade operacional crítica"
    elif 40 <= valor <= 69:
        classificacao = "ATENÇÃO"
        msg = "Estabilidade operacional reduzida"
    else:
        classificacao = "NORMAL"
        msg = "Estabilidade operacional adequada"
    return classificacao, msg

def calcular_pontuacao(classificacao):
    if classificacao == "CRÍTICO":
        return 2
    elif classificacao == "ATENÇÃO":
        return 1
    else:
        return 0

def classificar_ciclo(pontuacao):
    if  pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def identificar_area_mais_afetada(pontuacoes):
    maior_pont  = 0
    indice_area = 0

    for j in range(len(pontuacoes)):
        if pontuacoes[j] > maior_pont:
            maior_pont  = pontuacoes[j]
            indice_area = j

    return areas_monitoradas[indice_area]

def gerar_recomendacao(class_temperatura, class_comunicacao, class_bateria, class_oxigenio, class_estabilidade):

    if class_temperatura == "CRÍTICO" and class_comunicacao == "CRÍTICO" and class_bateria == "CRÍTICO" and class_oxigenio == "CRÍTICO" and class_estabilidade == "CRÍTICO":
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."

    if class_temperatura == "ATENÇÃO" and class_comunicacao == "ATENÇÃO" and class_bateria == "ATENÇÃO" and class_oxigenio == "ATENÇÃO" and class_estabilidade == "ATENÇÃO":
        return "Monitorar sistemas em atenção e preparar plano de contingência."

    if class_temperatura == "CRÍTICO":
        return "Verificar controle térmico da missão."
    if class_comunicacao == "CRÍTICO":
        return "Restabelecer contato com a base."
    if class_bateria == "CRÍTICO":
        return "Ativar modo de economia de energia."
    if class_oxigenio == "CRÍTICO":
        return "Acionar protocolo de suporte à vida."
    if class_estabilidade == "CRÍTICO":
        return "Reduzir operações não essenciais."

    if class_temperatura == "ATENÇÃO":
        return "Monitorar temperatura."
    if class_comunicacao == "ATENÇÃO":
        return "Monitorar comunicação."
    if class_bateria == "ATENÇÃO":
        return "Monitorar nível de bateria."
    if class_oxigenio == "ATENÇÃO":
        return "Monitorar nível de oxigênio."
    if class_estabilidade == "ATENÇÃO":
        return "Monitorar estabilidade operacional."

    return "Manter operação normal e continuar monitoramento."

def classificar_missao(risco_medio):
    if risco_medio <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco_medio <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def analisar_tendencia(riscos):

    primeiro = riscos[0]
    ultimo = riscos[-1]

    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."

    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."

    else:
        return "A missão permaneceu estável."

print("============================================================")
print("✧ MISSION CONTROL AI ✧")
print("============================================================")
print(f"Missão: Operação Amaris Lumina")
print(f"Equipe: Equipe Amaris II")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print()

for i in range(len(dados_missao)):
    ciclo = dados_missao[i]
    temperatura  = ciclo[0]
    comunicacao  = ciclo[1]
    bateria      = ciclo[2]
    oxigenio     = ciclo[3]
    estabilidade = ciclo[4]

    class_temperatura, msg_temperatura = analisar_temperatura(temperatura)
    class_comunicacao, msg_comunicacao = analisar_comunicacao(comunicacao)
    class_bateria, msg_bateria = analisar_bateria(bateria)
    class_oxigenio, msg_oxigenio = analisar_oxigenio(oxigenio)
    class_estabilidade, msg_estabilidade = analisar_estabilidade(estabilidade)

    ciclo_pont = (calcular_pontuacao(class_temperatura) + calcular_pontuacao(class_comunicacao) + calcular_pontuacao(class_bateria) + calcular_pontuacao(class_oxigenio) + calcular_pontuacao(class_estabilidade))
    ciclo_class = classificar_ciclo(ciclo_pont)
    ciclo_rec = gerar_recomendacao(class_temperatura, class_comunicacao, class_bateria, class_oxigenio, class_estabilidade)

    total_temperatura += temperatura
    total_comunicacao += comunicacao
    total_bateria += bateria
    total_oxigenio += oxigenio
    total_estabilidade += estabilidade
    riscos.append(ciclo_pont)
    pontuacoes_area[0] += calcular_pontuacao(class_temperatura)
    pontuacoes_area[1] += calcular_pontuacao(class_comunicacao)
    pontuacoes_area[2] += calcular_pontuacao(class_bateria)
    pontuacoes_area[3] += calcular_pontuacao(class_oxigenio)
    pontuacoes_area[4] += calcular_pontuacao(class_estabilidade)

    print("------------------------------------------------------------")
    print(f"CICLO {i + 1}")
    print("------------------------------------------------------------")
    print(f"Temperatura: {temperatura} °C | Classificação: {class_temperatura} | {msg_temperatura} ")
    print(f"Comunicação: {comunicacao}% | Classificação: {class_comunicacao} | {msg_comunicacao}")
    print(f"Bateria: {bateria}% | Classificação: {class_bateria} | {msg_bateria}")
    print(f"Oxigênio: {oxigenio}% | Classificação: {class_oxigenio} | {msg_oxigenio}")
    print(f"Estabilidade: {estabilidade}% | Classificação: {class_estabilidade} | {msg_estabilidade}")
    print(f"Pontuação de risco do ciclo: {ciclo_pont}")
    print(f"Classificação do ciclo: {ciclo_class}")
    print(f"Recomendação: {ciclo_rec}")

n = len(dados_missao)

media_temp = total_temperatura / n
media_com = total_comunicacao / n
media_bat = total_bateria / n
media_oxi = total_oxigenio / n
media_est = total_estabilidade / n
risco_medio = sum(riscos) / n
tendencia = analisar_tendencia(riscos)
maior_risco = 0
ciclo_critico = 0
qtd_criticos = 0
class_missao = (classificar_missao(risco_medio))
maior_area = identificar_area_mais_afetada(pontuacoes_area)

for j in range(len(riscos)):
    if riscos[j] > maior_risco:
        maior_risco = riscos[j]
        ciclo_critico = j + 1
    if riscos[j] >= 6:
        qtd_criticos += 1




print("------------------------------------------------------------")
print("RELATÓRIO FINAL DA MISSÃO")
print("============================================================")
print()
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print()
print(f"Média de temperatura: {media_temp:.2f} °C")
print(f"Média de comunicação: {media_com:.2f}%")
print(f"Média de bateria: {media_bat:.2f}%")
print(f"Média de oxigênio: {media_oxi:.2f}%")
print(f"Média de estabilidade: {media_est:.2f}%")
print()
print(f"Ciclo mais crítico: {ciclo_critico}")
print(f"Maior pontuação de risco: {maior_risco}")
print(f"Risco médio da missão: {risco_medio:.2f}")
print(f"Quantidade de ciclos críticos: {qtd_criticos}")
print()
print(f"Tendência da missão:")
print(tendencia)
print()
print(f"Pontuação acumulada por área: ")
print(f"Temperatura interna: {pontuacoes_area[0]}")
print(f"Comunicação com a base: {pontuacoes_area[1]}")
print(f"Sistema de energia: {pontuacoes_area[2]}")
print(f"Suporte de oxigênio: {pontuacoes_area[3]}")
print(f"Estabilidade operacional: {pontuacoes_area[4]}")
print()
print(f"Área mais afetada:")
print(maior_area)
print()
print(f"Classificação final da missão:")
print(class_missao)
print()
print(f"Conclusão:")
print()