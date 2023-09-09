import matplotlib.pyplot as plt
import csv
dict = {}

def carregaDados():
    arq = open("OK_Anexo_Arquivo_Dados_Projeto.csv", "r")
    coluna = csv.DictReader(arq, delimiter=";")
    for linha in coluna:
        for chave, valor in linha.items():
            if chave not in dict:
                dict[chave] = []
            dict[chave].append(valor)       
    arq.close()

def sumario():
    mesInicial = input("Digite o mês inicial (ex: 05, 06): ")
    anoInicial = input("Digite o ano inicial (ex: 2012, 2013): ")
    mesFinal = input("Digite o mês final (ex: 05, 06): ")
    anoFinal = input("Digite o ano final (ex: 2012, 2013): ")
    if validaMes(mesInicial, mesFinal) == True and validaAno(anoInicial, anoFinal) == True:
        periodoInicial = "01/" + mesInicial + "/" + anoInicial 
        dia = retornaDiasDoMes(mesFinal)
        periodoFinal = str(dia) + "/" + mesFinal + "/" + anoFinal
        if periodoInicial in dict["data"]:
            indexInicial = dict["data"].index(periodoInicial)
        if periodoFinal in dict["data"]:
            indexFinal = dict["data"].index(periodoFinal)
        opcao = input("Informe quais dados você quer ver: 1. todos, 2. apenas precipitação, 3. apenas temperatura, 4. apenas os de umidade e vento: ")
        for i in range(indexInicial, indexFinal + 1):
            if opcao == "1":
                print("Data: ", dict["data"][i], " Precipitação: ", dict["precip"][i], " Máxima: ",  dict["maxima"][i], " Mínima: ", dict["minima"][i], " Horas Insol: ", dict["horas_insol"][i], " Temperatura Média: ", dict["temp_media"][i], " Umidade Relativa: ", dict["um_relativa"][i], " Velocidade do vento: ", dict["vel_vento"][i])
            elif opcao == "2":
                print("Data: ", dict["data"][i], " Precipitação: ", dict["precip"][i])
            elif opcao == "3":
                print("Data: ", dict["data"][i], " Máxima: ",  dict["maxima"][i], " Mínima: ", dict["minima"][i])
            elif opcao == "4":
                print("Data: ", dict["data"][i], " Umidade Relativa: ", dict["um_relativa"][i], " Velocidade do vento: ", dict["vel_vento"][i])
            else: 
                print("Você digitou um valor inválido.")
    else:
        print("Esta data é inválida.")

def validaMes(mesInicial, mesFinal):
    if mesInicial.isdigit() and mesFinal.isdigit() == True:
        if int(mesInicial) > 0 and int(mesInicial) < 13 and int(mesFinal) > 0 and int(mesFinal) < 13:
            return True
        return False
    else: 
        print("Este valor é inválido.")
    
def validaAno(anoInicial, anoFinal):
    if anoInicial.isdigit() == True and anoFinal.isdigit() == True:
        if int(anoInicial) >1960 and int(anoInicial) < 2017 and int(anoFinal) >1960 and int(anoFinal) < 2017:
            return True
        return False
    else:
        print("Este valor é inválido.")

def retornaDiasDoMes(mesDigitado):
    if mesDigitado == '02':
        dias = 28
    elif mesDigitado =='04' or mesDigitado == '06' or mesDigitado == '09' or mesDigitado == '11':
        dias = 30
    else :
        dias = 31

    return dias
    
def retornaStringDoMes(mesdigitado):
    if mesdigitado == '01':
        nomedomes = "janeiro"
    elif mesdigitado == '02':
        nomedomes = "fevereiro"
    elif mesdigitado == '03':
        nomedomes = "março"
    elif mesdigitado == '04':
        nomedomes = "abril"
    elif mesdigitado == '05':
        nomedomes = "maio"
    elif mesdigitado == '06':
        nomedomes = "junho"
    elif mesdigitado == '07':
        nomedomes = "julho"
    elif mesdigitado == '08':
        nomedomes = "agosto"
    elif mesdigitado == '09':
        nomedomes = "setembro"    
    elif mesdigitado == '10':
        nomedomes = "outubro"
    elif mesdigitado == '11':
        nomedomes = "novembro"
    else:
        nomedomes = "dezembro"
    
    return nomedomes

def retornaMinima():
    anoinicial = 2005
    mesDigitado = input("Digite, por número, o mês que você quer saber a temperatura mínima dos últimos 11 anos (digite 04, 05): ")
    listaDatas = []
    listaDasMinimas = []
    mesporEscrito = retornaStringDoMes(mesDigitado)
    for i in range(11):
        somaDaMinina = 0
        anoinicial = anoinicial + 1
        dataDigitada = "01/" + mesDigitado + "/" + str(anoinicial)
        dias = retornaDiasDoMes(mesDigitado)
        if dataDigitada in dict["data"]:
            indexDaData = dict["data"].index(dataDigitada)
        for j in range(dias - 1):
            somaDaMinina = somaDaMinina + float(dict["minima"][indexDaData + j])    
        mediaDasMinimas = somaDaMinina/dias
        listaDasMinimas.append(mediaDasMinimas)
        listaDatas.append(anoinicial)
        print(f"Média do mês de {mesporEscrito} do ano de {anoinicial}: {listaDasMinimas[i]:.2f}")   
    plt.bar(listaDatas, listaDasMinimas)
    plt.title("Temperatura mínima nos últimos 11 anos")
    plt.xlabel("ano")
    plt.ylabel("mínima")
    plt.gcf().autofmt_xdate()
    plt.show()

carregaDados()
sumario()
retornaMinima()