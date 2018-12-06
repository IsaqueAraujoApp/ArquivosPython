#EXE1
#int -> int
def somacubo(n):
    "Funcao que retorna a soma dos cubus de 1 a n"
    if n == 1:
        return n
    return n**3 + somacubo(n-1)
#EXE2
#int, int -> int
def potencia(x, y):
    "Funcao que retorna a potencia de um numero x elevado a y"
    if y == 1:
        return x
    elif y == 0:
        return 1
    return x * potencia(x, y-1)
#EX3
#list -> int
def produtolista(lista):
    "Funcao que retorna a soma de todos os elementos de umas lista"
    if len(lista) == 1:
        return lista[0]
    return lista[0] * produtolista(lista[1:])
#EXE4
#int -> float
def somaparcela(n):
    "Funcao que retorna a soma de n parcelas"
    if n == 1:
        return (n**2+1.0)/(n+3)
    return (n**2+1.0)/(n+3) + somaparcela(n-1)
#EXE5
#string -> bool
def palindrimo(s):
    "Funcao que verifica se uma string e um palindrimo"
    if len(s) == 1 or len(s) == 0:
        return True
    elif s[0] != s[len(s)-1]:
        return False
    return palindrimo(s[1:-1])
#EXE6
#int, int -> int
def mdc(x, y):
    "Funcao que retorna o maior devisor comum entre dois numeros"
    if  y == 0:
        return x
    return mdc(y, x%y)
#EXE7
#int -> int
def binario(n):
    "Funcao que transforma um inteiro para forma binaria"
    if n == 1:
        return str(n%2)
    return binario(n/2)+str(n%2)
#DESAFIO
#INCOMPLETO, AINDA NAO ENCONTREI SOLUCAO SASTIFATORIA
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
 


    
    
    
