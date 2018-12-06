from random import randint
def teste():
    for x in range(1, 11):
        for y in range(1, 11):
            print '%d * %d = %d' % (x, y, x*y)
def soma():
    soma = 0
    for a in range(10):
        numero = randint(1,5)
        print numero
        soma = soma + numero
    return soma
def somaPar():
    lista = range(1,11,2)
    soma = 0
    for a in lista:
        soma +=a
    return soma
def fatorial(n):
    fatorial = 1
    for a in range(1,n+1):
        fatorial = fatorial*a
    return fatorial
def seq(n):
    soma = 0
    for a in range(1,n+1):
        soma += (a*2.0-1)/a
    return soma
def seq2(n):
    soma = 0
    for a in range(1,n+1):
        if a%2==0:
            soma-=(a*1.0)/(a**a)
        else:
            soma+=(a*1.0)/(a**a)                    
    return soma
def n(j, l):
    aux = 0
    for a in j:
        aux+=1
        if a[0] == l:
            return aux-1
        
                                    
    
