from random import randint
#EXE 1
#int -> int
def somaN(n):
    "Funcao que retorna a soma dos numeros impares dado um numero"
    soma = 0
    for a in range(1,n+1,2):
        soma+=a
    return soma
#EXE 2
#int, int -> list
def listaaleatorio(n,x):
    "Funcao que retorna uma lista com n elementos e cada elemento e um aleatorio entre 1 e x"
    lista = []
    for a in range(0,n):
        lista.append(randint(1,x))
    return lista
#EXE 3
#int, int -> string
def entreXeY(x,y):
    "Funcao que imprime na tela todos os numeros entre x e y"
    for a in range(x+1,y):
        print a
#EXE 4
#int -> int        
def somaParcela(n):
    "Funcao que retorna as n primeiras parcelas"
    soma = 0
    denominador = 1
    for a in range(1,n+1):
        if a%2 == 0:
            soma-=(1.0/denominador)
            print 1.0/denominador
            print "+"
        else:
            soma+=(1.0/denominador)
            print 1.0/denominador
            print "-"
        denominador+=2
#EXE 5
#int -> string
def numeroPerfeito(n):
    "Funcao que verifica se o numero e perfeito"
    lista = []
    for a in range(1,n):
        if n%a==0:
            lista.append(a)
    if sum(lista) == n:
        return "Perfeito"
    else:
         return "Imperfeito"
#EXE 6
#list ->int, int
def listaParImpar(lista):
    "Funcao que verifica a quantidade de numeros pares e impares dentro de uma lista"
    Qimpar = 0
    Qpar = 0
    for a in lista:
        if a%2 == 0:
            Qpar+=1
        else:
            Qimpar+=1
    return Qimpar, Qpar
#EXE 7
#list -> int
def MaisProximo(lista):
    "Funcao que retorna o indice do elemento mais proximo da media"
    media = sum(lista)/(len(lista)*1.0)
    diferenca = []
    indice = []
    for a in lista:
        diferenca.append(abs((a-media)))
    indiceN = 0
    for e in diferenca:
        if e == min(diferenca):
            indice.append(indiceN)
        indiceN+=1
    return indice
#EXE 8
#list -> int
def listastring(lista):
    "Funcao que retorna o indice de uma lista que contem o maior comprimento de string"
    listaTamanho = []
    for a in lista:
        listaTamanho.append(len(a))
    return listaTamanho.index(max(listaTamanho))
#EXE 9
#string -> string
def LinguaP(palavra):
    "Funcao que transforma uma palavra pra linguagem do P"
    palavranova = ""
    for a in palavra:
        palavranova+=a
        if a == "a":
            palavranova+="pa"
        if a == "e":
            palavranova+="pe"
        if a == "i":
            palavranova+="pi"
        if a == "o":
            palavranova+="po"
        if a == "u":
            palavranova+="pu"
    return palavranova
#EXE 10
#list, list -> string
def ListaAprovadoReprovado(listanome, listanota):
    "Funcao que printa se cada aluno de uma lista esta aprovado ou reprovado"
    indice = 0
    for a in listanota:
        if a < 5:
            print str(listanome[indice])+" - "+ "Reprovado"
        elif a >= 5:
            print str(listanome[indice])+" - "+ "Aprovado"
        indice+=1
    
            

            


    
    

            
    
            
    

