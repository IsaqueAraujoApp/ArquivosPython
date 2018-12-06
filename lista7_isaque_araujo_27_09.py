from random import randint
#EXE 1
#int -> int
def fatorial(n):
    "Funcao que retorna o valor do fatorial de um numero n"
    somafatorial = 1
    i = 0
    while i <n:
        somafatorial+=somafatorial*i
        i+=1
    return somafatorial
#EXE 2
#int -> int
def somaserie(n):
    "Funcao que retorna a soma dos n primeiros numeros de uma seguinte serie"
    soma = 1
    i = 1
    while i < n:
        soma +=((i+1.0)/(i+2.0)) 
        i+=1
    return soma
#EXE 3
#->int
def dado():
    "Funcao que retorna um dado e retorna a quantiade de vezes que ele foi jogado ate sair um numero repetido"
    primeirosorteado = randint(1,6)
    segundosorteado = randint(1,6)
    i = 1
    #print primeirosorteado
    while primeirosorteado != segundosorteado:
        primeirosorteado = randint(1,6)
        segundosorteado = randint(1,6)
        #print segundosorteado
        i+=1
    return i
#EXE 4
#int -> list
def divisores(n):
    "Funcao que dado um valor n retorna uma lista com todos os divisores de n"
    lista = []
    i = 1
    while i <= n:
        if n%i == 0:
            lista.append(i)
        i+=1
    return lista
#EXE 5
#int -> boolean
def primo(n):
    "Funcao que verifica se o numero e primo"
    if len(divisores(n)) == 2:
        return True
    return False
#EXE 6
#int, int -> list
def listaprimo(x,y):
    "Funcao que dado dois numeros retorna todos os numeros primos entre esses dois numeros"
    listacriada = range(x+1,y)
    listaprimo = []
    i = 0
    while i < len(listacriada):
        if primo(listacriada[i]) == True:
            listaprimo.append(listacriada[i])
        i+=1
    return listaprimo
#EXE 7
#int
def Populacao():
    "Funcao que calcula a quantidade de anos para a populacao de A ser maior ou igual a B"
    QuantA = 80000
    QuantB = 200000
    TaxaA = 0.03
    TaxaB = 0.015
    cont = 0
    while QuantA <= QuantB:
        QuantA = QuantA + QuantA*TaxaA
        QuantB = QuantB + QuantB*TaxaB
        cont+=1
    return cont
#EXE 8
#int, int, float, float -> int
def PopulacaoFicticia(QuantA, QuantB, TaxaA, TaxaB):
    "Funcao que calcula a quantidade de anos para a populacao de A ser maior ou igual a B"
    cont = 0
    if TaxaA <= TaxaB:
        return "A populacao A nunca ultrapassar a B, pois a taxa de crescimento de A e menor"
    else:
        while QuantA <= QuantB:
            QuantA = QuantA + QuantA*TaxaA
            QuantB = QuantB + QuantB*TaxaB
            cont+=1
        return cont
#EXE 9
#list, string -> string
def ListaNomes(lista, letra):
     "Funcao que retorna os nomes de uma lista caso eles comecem com uma certa letra definida"
     i = 0
     listacomnomes = []
     while i < len(lista):
         nome = lista[i]
         if nome[0:1] == letra:
             listacomnomes.append(lista[i])
             print nome
         i+=1
     if len(listacomnomes) == 0:
         return "Nao ha nome comecando com a letra"
#EXE 10
#int -> int
def Fibonacci(n):
    "Funcao que retorna todos os numeros de uma sequencia fibonacci que sejam menores que n"
    listaFibonacci = [0,1]
    cont = 0
    while listaFibonacci[len(listaFibonacci)-1] < n:
        listaFibonacci.append(listaFibonacci[cont]+listaFibonacci[cont+1])
        cont+=1
    print listaFibonacci
    i = 0
    while i < len(listaFibonacci):
        if listaFibonacci[i] < n:
            print listaFibonacci[i]
        i+=1
#EXE 11
#list, list -> list
def ListaMediaAluno(L1, L2):
    "Funcao que dado uma lista com nomes e outra com notas retorna uma lista com o nome e a nota dos alunos que ficaram acima da media"
    media = sum(L2)/len(L2)
    i = 0
    listamedia = []
    while i < len(L2):
        if L2[i]> media:
            listamedia.append((L1[i], L2[i]))
        i+=1
    return listamedia
   
        
