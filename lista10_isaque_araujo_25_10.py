from random import randint
#EXE 1
#matriz, matriz -> matriz
def matrizaleatoria(x, y):
    matriz = []
    aleatorios  = []
    i = 0
    while i < x:
        j = 0
        aleatorios = []
        while j < y:
            aleatorios.append(randint(1,10))
            j+=1
        matriz.append(aleatorios)
        i+=1
    return matriz
#EXE 2
#int -> matriz 
def matrizidentidade(n):
    matriz = []
    i = 0
    while i < n:
        matriz.append([0]*n)
        matriz[i][i] = 1
        i+=1
    return matriz
#EXE 3
#matriz, int -> int
def NumeroNaMatriz(matriz, x):
    count = 0
    for a in matriz:
        for b in a:
            if b == x:
                count+=1    
    return count
#EXE 4
#matriz -> int, int
def maxmatriz(matriz):
    maxlinha = 0
    maxcoluna = 0
    maximo = 0
    count = 0
    for a in matriz:
        for b in a:
            if b > maximo:
                maximo = b
                maxlinha = count
                maxcoluna = a.index(max(a))
        count+=1
    return maxlinha, maxcoluna
#EXE 5
#matriz -> matriz
def matriztransposta(matriz):
    linhas = []
    colunas = []
    i = 0
    while i < len(matriz[0]):
        colunas = []
        for a in matriz:
            colunas.append(a[i])
        linhas.append(colunas)
        i+=1
    return linhas
#EXE 6
#matriz -> float
def matrizCR(matriz):
    cr = 0
    div = 0
    for a in matriz:
        cr+=a[0]*a[1]
        div+=a[1]
    return cr/div
#EXE 7
#matriz -> string, int
def matrizfuncionario(matriz):
    setor = raw_input()
    for a in matriz:
        if a[2] == setor:
            print "Nome:",a[0], "Registro:",a[1]
#EXE 8
#matriz, matriz -> matriz
def multmatriz(m1, m2):
    linhas = []
    colunas = []
    i = 0
    j = 0
    valor  = 0
    if len(m1[0]) == len(m2):
        while j < len(m1):
            colunas = []
            for a in m1:
                valor = 0
                i = 0
                while i < len(m1[0]):
                    valor+=a[i]*m2[i][j]
                    i+=1
                colunas.append(valor)
            linhas.append(colunas)
            j+=1
        return matriztransposta(linhas)  
    else:
        return "Para multiplicar matrizes o numero de colunas da primeira deve ser igual o numero de linhas da segunda"
#multmatriz([[2,3],[0,1],[-1,4]], [[1,2,3],[-2,0,4]])
def mult(m1,m2):
    linhas = []
    colunas = []
    i = 0
    j = 0
    valor = 0
    for a in m1:
        colunas = []
        j = 0
        for b in m2[0]:
            valor = 0
            i = 0
            for c in a:
                valor+=c*m2[i][j]
                i+=1
            colunas.append(valor)
            j+=1
        linhas.append(colunas)
    return linhas
            
    
        
            
    
    

    
