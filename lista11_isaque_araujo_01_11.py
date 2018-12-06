#EXE1
#string -> dictionary
def dicionariocontador(s):
    "Funcao que recebe uma frase e a transforma em um dicionario, cada chave do dicionario e uma palavra da string, e o valor da chave e quantidade de vezes que a palavra aparece na frase"
    #s = "sabia que a m~ae do sabi´a sabia que sabi´a sabia assobiar"
    d = {}
    for i in s.split():
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    return d
#EXE2
#string -> dictionary
def dicionariocaracter(s):
    "Funcao que recebe uma frase e a transforma em um dicionario. Cada chave do dicionario e a letra inicial de cada palavra, e o valor de cada chave sao as palavras que comecam com essa letra"
    #s = "tr^es pratos de prata de trigo para tr^es tristes tigres"
    d = {}
    for i in s.split():
        if i[0] in d:
            if list.count(d[i[0]], i) == 0:
                d[i[0]]+=[i]
        else:
            d[i[0]] = [i]
    return d
#EXE3
#string, dictionary -> string
def tradutor(s, d):
    "Funcao que recebe uma string e um dicionario. Ocorre a traducao da frase"
    #s = "eu gosto de programacao"
    #d = {"gosto":"like","programacao":"programming"}
    lista = []
    for i in s.split():
        if i in d:
            lista.append(d[i])
        else:
            lista.append(i)
    return str.join(" ", lista)
#EXE4
#dictionary, dictionary -> float
def calculapreco(lista_de_compras, supermercado):
    "Funcao que calcula o preco de uma lista de compras usando dois dicionarios"
    preco = 0
    #lista_de_compras = {"biscoito":3, "chocolate":2, "farinha":1}
    #supermercado = { "amaciante":4.99, "arroz":10.90, "biscoito":1.69, "cafe":6.98, "chocolate":3.79,"farinha":2.99}
    for i in lista_de_compras:
        preco+=lista_de_compras[i]*supermercado[i]
    return preco
#EXE5
#list, list -> dictionary
def media(nomes, notas):
    "Funcao que recebe duas listas, uma com nomes e outra com notas. A funcao retorna um dicionario com a media de cada aluno"
    d = {}
    #nomes = ["Pedro","Ana","Felipe"]
    #notas = [[7.5,9.5],[8.0,10.0],[6.0,9.0]]
    i = 0
    for nome in nomes:
        d[nome]=sum(notas[i])/len(notas[i])
        i+=1
    return d
#EXE 6
#dictionary -> list
def afinidades(afinidades):
    "Funcao que recebe um dicionario de afinidades e retorna uma lista com casais"
    #afinidades = {"Leo": "Sofia","Marcos": "Andrea","Sofia": "Leo","Alex": "Andrea","Andrea": "Marcos"}
    lista = []
    for nome in afinidades:
        if nome == afinidades[afinidades[nome]] and afinidades[afinidades[nome]] == nome:
            lista.append((nome, afinidades[nome]))
            afinidades[nome] = " "
    return lista
    
