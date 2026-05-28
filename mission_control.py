dados_missao =[
[24, 92, 88, 96, 90],
[27, 80, 72, 94, 85],
[31, 65, 58, 91, 70],
[36, 42, 38, 87, 55],
[39, 28, 19, 78, 35],
[34, 55, 32, 82, 50]]

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
    if  pontuacao < 2:
        return "MISSÃO ESTÁVEL"
    elif 3 <= pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def gerar_recomendacao(class_temp, class_com, class_bat, class_oxi, class_est):
    classificacoes = [class_temp, class_com, class_bat, class_oxi, class_est]

    todos_criticos = True
    todos_atencao = True

    for j in range(len(classificacoes)):
        if classificacoes[j] != "CRÍTICO":
            todos_criticos = False
        if classificacoes[j] != "ATENÇÃO":
            todos_atencao = False

    if todos_criticos:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."

    if todos_atencao:
        return "Monitorar sistemas em atenção e preparar plano de contingência."

    msgs_critico = [
        "Verificar controle térmico da missão.",
        "Restabelecer contato com a base.",
        "Ativar modo de economia de energia.",
        "Acionar protocolo de suporte à vida.",
        "Reduzir operações não essenciais."
    ]

    msgs_atencao = [
        "Monitorar temperatura.",
        "Monitorar comunicação.",
        "Monitorar nível de bateria.",
        "Monitorar nível de oxigênio.",
        "Monitorar estabilidade operacional."
    ]

    recomendacao = ""

    for j in range(len(classificacoes)):
        if classificacoes[j] == "CRÍTICO":
            recomendacao += msgs_critico[j] + " "
        elif classificacoes[j] == "ATENÇÃO":
            recomendacao += msgs_atencao[j] + " "

    if recomendacao == "":
        recomendacao = "Manter operação normal e continuar monitoramento."

    return recomendacao

def analisar_tendencia(riscos):

    primeiro = riscos[0]
    ultimo = riscos[-1]

    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."

    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."

    else:
        return "A missão permaneceu estável."

print(f"============================================================")
print(f"✧ MISSION CONTROL AI ✧")
print(f"============================================================")
print(f"Missão: Operação Amaris Lumina")
print(f"Equipe: Equipe Amaris")
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
    recomendacoes = gerar_recomendacao(class_temperatura, class_comunicacao, class_bateria, class_oxigenio, class_estabilidade)

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

    print(f"------------------------------------------------------------")
    print(f"CICLO {i + 1}")
    print(f"------------------------------------------------------------")
    print(f"Temperatura: {ciclo[0]} °C | Classificação: {class_temperatura} | {msg_temperatura} ")
    print(f"Comunicação: {ciclo[1]}% | Classificação: {class_comunicacao} | {msg_comunicacao}")
    print(f"Bateria: {ciclo[2]}% | Classificação: {class_bateria} | {msg_bateria}")
    print(f"Oxigênio: {ciclo[3]}% | Classificação: {class_oxigenio} | {msg_oxigenio}")
    print(f"Estabilidade: {ciclo[4]}% | Classificação: {class_estabilidade} | {msg_estabilidade}")
    print(f"Pontuação de risco do ciclo: {ciclo_pont}")
    print(f"Classificação do ciclo: {ciclo_class}")
    print(f"Recomendação: {recomendacoes}")

n = len(dados_missao)

media_temp = total_temperatura / n
media_com  = total_comunicacao / n
media_bat  = total_bateria     / n
media_oxi  = total_oxigenio    / n
media_est  = total_estabilidade / n
risco_medio = sum(riscos) / n
tendencia = analisar_tendencia(riscos)

print(f"------------------------------------------------------------")
print(f"RELATÓRIO FINAL DA MISSÃO")
print(f"============================================================")
print()
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print()
print(f"Média de temperatura: {media_temp:.2f} °C")
print(f"Média de comunicação: {media_com:.2f}%")
print(f"Média de bateria: {media_bat:.2f}%")
print(f"Média de oxigênio: {media_oxi:.2f}%")
print(f"Média de estabilidade: {media_est:.2f}%")
print()
print(f"Ciclo mais crítico:")
print(f"Maior pontuação de risco:")
print(f"Maior pontuação de risco:")
print(f"Risco médio da missão: {risco_medio:.2f}")
print(f"Quantidade de ciclos críticos:")
print()
print(f"Tendência da missão:")
print(tendencia)
print()
print(f"Pontuação acumulada por área: ")
print(f"Temperatura interna: ")
print(f"Comunicação com a base: ")
print(f"Sistema de energia: ")
print(f"Suporte de oxigênio: ")
print(f"Estabilidade operacional: ")
print()
print(f"Área mais afetada:")
print()
print()
print(f"Classificação final da missão:")
print()
print()
print(f"Conclusão:")
print()