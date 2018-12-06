def zeus(L):
    n = len(L)
    aux = [0]*n
    return L+aux
def alteraLista(lista):
    list.append(lista,10)
    list.append(lista,[3,'bola'])
    list.append(lista,'lua')
    list.extend(lista,[1,2,3])
    list.extend(lista,'lua')
    del lista[2]
    list.insert(lista,2,1)
    list.remove(lista,2)
    elemento = list.pop(lista,3)
    list.insert(lista,1,elemento)
    return lista

def Coulumb(Q1, Q2,d):
    return (8.98*(10**9))((Q1*Q2)/(d**2))
def Retangulo(x,y):
    return x*y
def Hipo(cat1, cat2):
    return ((cat1**2+cat2**2))**(1/2.0)
def permutacao():
    l1 = [1,2,3]
    l2 = [2,1,3]
    count = 0
    for a in l1:
        if l1.count(a) == l2.count(a):
            count+=1
        else:
            return False
    if count == len(l1):
        return True
def permutacao2():
    l1 = [1,2,3]
    l2 = [2,1,3]
    d1 = {}
    d2 = {}
    count  = 0
    contador1 = 0
    contador2 = 0
    for i in l1:
        contador1+=1
    for j in l2:
        contador2+=1
    if contador1 == contador2:
        for a in l1:
            if a not in d1:
                d1[a] = 1
            else:
                d1[a]+=1
        for b in l2:
            if b not in d2:
                d2[b] = 1
            else:
                d2[b]+=1
        for d in d1:
            if d1[d] == d2[d]:
                count+=1
            else:
                return False
        if count == contador1 or contador2:
            return True
    else:
        return False
def e_permutacao (a, b):
    if len ( a ) == 0:
        return len ( b )==0
    if a [0] not in b :
        return False
    i = b . index ( a [0])
    return e_permutacao ( a [1:] , b [: i ]+ b [ i +1:])
def inverte(palavra):
    resultado = ""
    i = len(palavra)-1
    while i >= 0:
        resultado+=palavra[i]
        i-=1
    return resultado
def permutacao(lista):
    Npermutacoes = 1
    permutacao = lista[:]
    Lpermutacoes = []
    N = len(lista)-1
    valor = 0
    j = 0
    for i in range(1,len(lista)+1):
        Npermutacoes = Npermutacoes*i
    Npermutacoes-=1
    while Npermutacoes > 0:
        valor = permutacao[j]
        del permutacao[j]
        permutacao.insert(j+1, valor)
        Lpermutacoes.append(permutacao[:])
        j+=1
        if j == N:
            j = 0
        Npermutacoes -=1
    return Lpermutacoes
def permuta(s, s1 = [], lista = []):
    if len(s) == 0:
        print lista
    else:
        for i in range(len(s)):
            if len(lista) == 0:
                lista.append(s1[:]+s[i:])
            elif s1[:]+s[i:] not in lista:
                if len(s1[:]+s[i:]) == len(lista[0]):
                    lista.append(s1[:]+s[i:])
            permuta(s[:i]+s[(i+1):],s1[:]+s[i:i+1])
def SomaElementoMultiplicaMatriz(matriz, n):
    soma = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[0])):
            soma+=matriz[i][j]
            matriz[i][j] = matriz[i][j]*n
    print soma
    print matriz
def MatrizIdentidade(n):
    matriz = []
    count = 0
    for i in range(0,n):
        matriz.append([0]*n)
        matriz[count][count] = 1
        count+=1
    return matriz
def Transposta(matriz):
    linhas = []
    colunas = []
    for i in range(0, len(matriz[0])):
        colunas = []
        for j in matriz:
            colunas.append(j[i])
        linhas.append(colunas)
    return linhas
def SomaOrMediaMatriz(matriz, linha, resultado):
    soma = 0
    for i in matriz[linha]:
        soma+=i
    media = soma/(len(matriz[0])*1.0)
    if resultado == "S":
        return soma
    else:
        return media
def SomaOrMediaMatriz2(matriz, coluna, resultado):
    soma = 0
    for i in matriz:
        soma+=i[coluna]
    media = soma/(len(matriz)*1.0)
    if resultado == "S":
        return soma
    else:
        return media
def SomaAcimaDiagonalPrincipal(matriz, resultado):
    soma = 0
    k = 1
    for i in matriz:
        for j in i[k:]:
            soma+=j
        k+=1
    return soma
def SomaAbaixoDiagonalPrincipal(matriz, resultado):
    soma = 0
    k = 1
    for i in matriz[1:]:
        for j in i[:k]:
            soma+=j
        k+=1
    return soma
def SomaAcimaDiagonalSecundaria(matriz, resultado):
    soma = 0
    k = 1
    for i in matriz:
        for j in i[:len(matriz)-k]:
            soma+=j
        k+=1
    return soma
def SomaAbaixoDiagonalSecundaria(matriz, resultado):
    soma = 0
    k = 1
    for i in matriz[1:]:
        for j in i[len(matriz)-k:]:
            soma+=j
        k+=1
    return soma
def SomaAreaSuperior(matriz, resultado):
    soma = 0
    k = 1
    for i in matriz:
        for j in i[k:len(matriz)-k]:
            soma+=j
        k+=1
    return soma
#Complexo
def SomaAreaDireita(matriz, resultado):
    soma = 0
    k = 1
    for i in matriz[1:]:
        for j in i[len(matriz)-k:]:
            print i[len(matriz)-k:]
            if len(i[len(matriz)-k:]) < 2:
                soma+=j
            k+=1
    return soma
def cubo(lista):
    if len(lista) == 1:
        return lista[0]**3
    return lista[0]**3+cubo(lista[1:])
def stop():
    x = input()
    while True:
        if x == 0:
            return "Finish"
        else:
            x = input()
def duplicados(lista):
    indice = 0
    for i in lista:
        if lista.count(i) > 1:
            lista[indice] = "X"
        indice+=1
    for j in lista:
        if j == "X":
            lista.remove(j)
    return lista
def DicionarioFrase(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d
def listadetuplas(lista):
    d = {}
    for i in lista:
        d[i[0]] = i[1]
    return d
def tuple(d):
    lista = []
    listaresultante = []
    for i in d:
        lista.append((i, d[i]))
    ordenacao = []
    for j in lista:
        ordenacao.append(j[0])
    ordenacao.sort()
    for k in ordenacao:
        listaresultante.append((k,d[k]))
    return listaresultante
def palavra():
    x = raw_input("Digite uma palavra")
    d = {}
    while True:
        if x != "fim":
            if x not in d:
                d[x] = 1
            else:
                d[x] +=1
            x = raw_input("Digite uma palavra")
        else:
            for i in d:
                print i, d[i]
            break
def fatorial(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    return n* fatorial(n-2)
def exe1():
    lista = [3,4,5,6]
    i = 0
    x = 5
    while i < 4:
        y = x-lista[i]
        print y
        x+= lista[i]*(lista[i]%3)
        i+=1
    return x
        
    
            



 
 

    
