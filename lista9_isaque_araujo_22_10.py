#EXE 1
#input(float), input(float), input(float), input(float) -> string, float
def diferenca():
    A = input()
    B = input()
    C = input()
    D = input()
    print "DIFERENCA =", (A*B-C*D)
#EXE 2
#input(int) -> (int, string)*3    
def ano():
    n = input()
    ano = 0
    meses = 0
    dias = 0
    ano+=(n/365)
    n = n-(ano*365)
    meses+=(n/30)
    n = n-(meses*30)
    dias+= (n/1)
    n = n-(dias*1)
    print ano, "ano(s)"
    print meses, "mes(es)"
    print dias, "dia(s)"
#EXE 3
#input(float), input(float) -> string    
def quadrante():
    x = input()
    y = input()
    if x == 0 and y != 0:
        print "Eixo Y"
    elif y == 0 and x !=0:
        print "Eixo X"
    elif x > 0 and  y > 0:
        print "Q1"
    elif x < 0 and y > 0:
        print "Q2"
    elif x < 0 and y < 0:
        print "Q3"
    elif x > 0 and y < 0:
        print "Q4"
    else:
        print "Origem"
#EXE 4
#input(float),input(float),input(float),input(float),input(float),input(float) -> int, string        
def positivo():
    i = 0
    lista = []
    positivos = 0
    while i < 6:
        x = input()
        lista.append(x)
        i+=1
    for a in lista:
        if a > 0:
            positivos+=1
    print positivos, "valores positivos"        
#EXE 5
#inpu(int) -> int, int, int, string    
def pum():
    n = input()
    a = 1
    b = 2
    c = 3
    i = 0
    while i < n*4:
        print a+i, b+i, c+i, "PUM"
        i+=4
#EXE 6
#int, input(int) -> string, int, string, int        
def caracoroa():
    n = input()
    i = 0
    lista = []
    mary = 0
    john = 0
    while i < n:
        lista.append(input())
        i+=1
    for a in lista:
        if a == 0:
            mary+=1
        else:
            john+=1
    print "Mary won", mary, "times and John won", john, "times"
#EXE 7
#input(int)*n, (input(float), input(float))*n -> (float, string)*n
def pipa():
    n = input()
    i = 0
    lista = []
    while i < n:
        parametrox, parametroy = input(), input()
        lista.append((parametrox *parametroy)/2)
        i+=1
    j = 0 
    while j < n:
        print lista[j], "cm2"
        j+=1
#EXE 8
#input(int), input(int), (input(int))*n -> int        
def album():
    Qalbum = input()
    Qcompradas = input()
    lista = []
    i = 1
    listacompleta = range(1,Qalbum+1)
    while i <= Qcompradas:
        x = input()
        lista.append(x)
        i+=1
    for a in lista:
        j = 0
        while j < len(listacompleta):
            if a == listacompleta[j]:
                listacompleta.remove(a)
            j+=1
    print len(listacompleta)
    
        
    

    
