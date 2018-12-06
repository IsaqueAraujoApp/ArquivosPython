import math
#EXE 1
#float -> float
def PesoIdealHomem(altura):
    return (72.7*altura)-58
#float -> float
def PesoIdealMulher(altura):
    return (62.1*altura)-44.7
#EXE 2
#float, string -> string
def PesoIdealHumano(altura, sexo):
    if sexo == "M" or sexo == "m":
        return PesoIdealHomem(altura)
    elif sexo == "F" or sexo == "f":
        return PesoIdealMulher(altura)
    else:
        return "O sexo informado e invalid, por favor, use M, m, F ou f"
#EXE 3
#float, string  -> string
def PesoIdealCerto(altura, peso, sexo):
    if sexo == "M" or sexo == "m":
        if PesoIdealHumano(altura, sexo) > peso:
            return "Abaixo do peso"
        elif PesoIdealHumano(altura,sexo) == peso:
            return "Peso Ideal"
        else:
            return "Acima do Peso"
    elif sexo == "F" or sexo == "f":
        if PesoIdealHumano(altura, sexo) > peso:
            return "Abaixo do peso"
        elif PesoIdealHumano(altura,sexo) == peso:
            return "Peso Ideal"
        else:
            return "Acima do Peso"
    else:
        return "Sexo e invalido"
#EXE 4
#int -> int, float
def FatorialRaiz(x):
    lista = range(x)
    lista.remove(0)
    lista.append(x)
    fatorial = 1
    i = 0
    while i < len(lista):
        fatorial += fatorial*i
        i+=1
    return  fatorial, math.sqrt(x)
#EXE 5
#int - string
def SinalParidade(x):
    if x == 0:
        return "Par e Zero"
    elif x > 0 and x%2==0:
        return "Positivo e Par"
    elif x > 0 and x%2 != 0:
        return "Positivo e Impar"
    elif x < 0 and x%2 == 0:
        return "Negativo e Par"
    else:
        return "Negativo e Impar"
#EXE 6
#string -> int
def QuantVogais(s):
    a = s.count("a")
    A = s.count("A")
    e = s.count("e")
    E = s.count("E")
    i = s.count("i")
    I = s.count("I")
    o = s.count("o")
    O = s.count("O")
    u = s.count("u")
    U = s.count("U")
    return "Quantidade de vogais na string e igual a " + str(a+A+e+E+i+I+o+O+u+U)
#EXE 7
#int -> int
def CaixaEletronico(valor):
    Notas100 = 0
    Notas50 = 0
    Notas10 = 0
    Notas5 = 0
    Notas1 =0
    Notas100+=(valor/100)
    valor = valor-(Notas100*100)
    Notas50+=(valor/50)
    valor = valor-(Notas50*50)
    Notas10+= (valor/10)
    valor = valor-(Notas10*10)
    Notas5+=(valor/5)
    valor = valor - (Notas5*5)
    Notas1+=(valor/1)
    valor = valor -(Notas1*1)
    return Notas100+Notas50+Notas10+Notas5+Notas1
#EXE 8
#float, float -> float
def ValorMacaMorango(maca, morango):
    valortotalcompra = 0
    Pmaca = 0
    Pmorango = 0
    if maca <= 5:
        Pmaca = 3.50
    else:
        Pmaca = 3.15
    if morango <= 5:
        Pmorango = 5.50
    else:
        Pmorango = 4.95
    valortotalcompra = maca*Pmaca+morango*Pmorango
    if (maca+morango) > 12 or valortotalcompra > 50:
        return valortotalcompra*0.9
    else:
        return valortotalcompra
#EXE 9
#string, string -> string, string
def TwoStringFormatada(s1,s2):
    palavra1 = ""
    palavra2 = ""
    if len(s1)%2 == 0:
        palavra1 = s1[:len(s1)/2]+s2[len(s2)/2:]
    else:
        palavra1 = s1[:len(s1)/2]+s2[len(s2)/2:]
    if len(s2)%2 == 0:
        palavra2 = s1[len(s1)/2:]+s2[:len(s2)/2]
    else:
        palavra2 = s1[len(s1)/2:]+s2[:len(s2)/2]
    return palavra1, palavra2
#EXE 10
#string -> int
def UltimoIndice(s, letra):
    if s.count(letra) > 0:
        sinvertida = s[::-1]
        return len(s)-1-sinvertida.index(letra),sinvertida 
    else:
        return "A letra nao existe na palavra"
#EXE 11
#int, int, int, int, int -> int
def MaiorNota(x1,x2,x3,x4,x5):
    nota1 = 0
    nota2 = 0
    maiornota12 = 0
    if x1 > x2:
        nota1 = x1
    elif x1 < x2:
        nota1 = x2
    else:
        nota1 = x1 or x2
    if x3 > x4:
        nota2 = x3
    elif x3 < x4:
        nota2 = x4
    else:
        nota2 = x3 or x4
    if nota1 > nota2:
        maiornota12 = nota1
    elif nota1 < nota2:
        maiornota12 = nota2
    else:
        maiornota12 = nota1 or nota2
    if maiornota12 > x5:
        return maiornota12
    elif maiornota12 < x5:
        return x5
    else:
        return maiornota12 or x5
#int, int, int, int, int -> int
def MenorNota(x1,x2,x3,x4,x5):
    nota1 = 0
    nota2 = 0
    menornota12 = 0
    if x1 > x2:
        nota1 = x2
    elif x1 < x2:
        nota1 = x1
    else:
        nota1 = x1 or x2
    if x3 > x4:
        nota2 = x4
    elif x3 < x4:
        nota2 = x3
    else:
        nota2 = x3 or x4
    if nota1 > nota2:
        menornota12 = nota2
    elif nota1 < nota2:
        menornota12 = nota1
    else:
        menornota12 = nota1 or nota2
    if menornota12 > x5:
        return x5
    elif menornota12 < x5:
        return menornota12
    else:
        return menornota12 or x5
#int, int, int, int, int -> int
def MediaFinal(x1,x2,x3,x4,x5):
    return (x1+x2+x3+x4+x5-MaiorNota(x1,x2,x3,x4,x5)-MenorNota(x1,x2,x3,x4,x5))/3.0
    
    
        
        
    
    
        
            
