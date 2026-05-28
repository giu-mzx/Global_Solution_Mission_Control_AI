dados_missao =[
[24, 92, 88, 96, 90],
[27, 80, 72, 94, 85],
[31, 65, 58, 91, 70],
[36, 42, 38, 87, 55],
[39, 28, 19, 78, 35],
[34, 55, 32, 82, 50]]

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

print(f"============================================================")
print(f"MISSION CONTROL AI")
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

    print(f"------------------------------------------------------------")
    print(f"CICLO {i + 1}")
    print(f"------------------------------------------------------------")
    print(f"Temperatura: {ciclo[0]} °C | Classificação: {class_temperatura} | {msg_temperatura} ")
    print(f"Comunicação: {ciclo[1]}% | Classificação: {class_comunicacao} | {msg_comunicacao}")
    print(f"Bateria: {ciclo[2]}% | Classificação: {class_bateria} | {msg_bateria}")
    print(f"Oxigênio: {ciclo[3]}% | Classificação: {class_oxigenio} | {msg_oxigenio}")
    print(f"Estabilidade: {ciclo[4]}% | Classificação: {class_estabilidade} | {msg_estabilidade}")
    print(f"Pontuação de risco do ciclo:: {ciclo_pont}")
    print(f"Classificação do ciclo: ")
    print(f"Recomendação: ")

print(f"------------------------------------------------------------")
print(f"RELATÓRIO FINAL DA MISSÃO")
print(f"============================================================")
