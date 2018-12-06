#EXE 1
#list, list -> list, list
def ListaAlterada(lista1, lista2):
    "Funcao que recebe duas listas e retorna a primeira com o primeiro elemento da segunda, e a segunda com o primero elemento da primeira"
    lista1.append(lista2[0])
    lista2.append(lista1[0])
    return lista1, lista2
#EXE 2
#list -> list
def ListaMeioNoFinal(s):
    "Funcao que recebe uma lista e reposiona os elementos centrais"
    lista = []
    lista.extend(s)
    meioimpars = s[len(s)/2:len(s)/2+1]
    #variavel abaixo pega o segundo elemento de uma lista par
    QuanEle = s[len(s)/2-1:len(s)/2]
    #variavel abaixo pega primeiro elemento de uma lista par
    QuanEle2 = s[:len(s)/2-1]
    meiopars = s[len(s)/2:]
    if len(s)%2 != 0:
        del lista[len(s)/2]
        lista.extend(meioimpars)
    else:
        lista = QuanEle2
        lista.extend(meiopars)
        lista.extend(QuanEle)
    return lista
#EXE 3
#list -> list
def Add0(lista):
    "Funcao que recebe uma lista e adiciona uma quantidade de 0 como novos elementos da lista"
    n = len(lista)
    zeros = "0"*n
    listadezeros = []
    listadezeros[:] = zeros
    return lista+listadezeros
#EXE 4
#list, int -> list
def RemoverMenor(lista):
    "Funcao que remove o menor elemento de uma lista"
    if lista.count(min(lista)) == 1:
        lista.pop(min(lista))
        return lista
    elif lista.count(min(lista)) > 1:
        lista.remove(min(lista))
        return lista
#EXE 5
#list, int -> list
def MenorNumeroEsquerda(lista, x):
    "Funcao que poem o numero escolhido a esquerda do menor numero da lista"
    menornumero = min(lista)
    indice = lista.index(menornumero)
    list.insert(lista, indice,x)
    return lista
#EXE 6
#string -> string
def InverteFrase(s):
    "Funcao que inverte a frase"
    lista = []
    lista.extend(str.split(s))
    lista.reverse()
    return str.join(" ", lista)
#EXE 7
#list, n -> list
def NumerosMaioresNaLista(lista, n):
    "Funcao que dado uma lista e um inteiro n retorna uma nova lista somentes com os numeros da lista original que sejam maiores que n"
    lis = []
    lis2 = []
    i = 0
    #metodo for
    for a in lista:
        if a > n:
            lis.append(a)
    #metodo while        
    while i < len(lista):
        if lista[i] > n:
            lis2.append(lista[i])
        i+=1
    return lis, lis2
#EXE 8
#list -> int
def SegundoMaior(lista):
    "Funcao que retorna o indice do segundo maior elemento da lista"
    indice = lista.index(max(lista))
    lista[indice] = 0
    return lista.index(max(lista))
#EXE 9
#list -> list
def MediaTurma(lista):
    "Funcao que retorna a media da turma e uma lista com as notas que ficaram acima da media"
    media = sum(lista)/(len(lista))
    notasacima = []
    notasacima2 = []
    i = 0
    #metodo for
    for a in lista:
        if a > media:
            notasacima.append(a)
    #metodo while
    while i < len(lista):
        if lista[i] > media:
            notasacima2.append(lista[i])
        i+=1
    return media, notasacima, notasacima2
#EXE 10
#int, int, int, int -> list, list
def ListaParListaImpar(n1,n2,n3,n4):
    "Funcao que dados 4 inteiros retorna uma lista com os numeros impares e outra com os pares"
    lista = []
    lista.append(n1)
    lista.append(n2)
    lista.append(n3)
    lista.append(n4)
    listapar = []
    listaimpar = []
    #metodo while
    for a in lista:
         if a%2 == 0:
             listapar.append(a)
         else:
             listaimpar.append(a)
    return listapar, listaimpar
    
    
        
