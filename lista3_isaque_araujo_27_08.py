#str,int -> str
def multPalavras(a, b):
    "funcao que recebe duas palavras, junta as duas e multiplica a palavra formada por 3"
    return (a+b)*3
#double, double, double -> double
def calcDelta(a, b, c):
    "funcao que calcula o delta dados 3 valores"
    return (b**2)-4*a*c
#double, double, double -> string
def quantRaizes(a, b, c):
    "funcao que verifica quantas raizez a equacao do 2 grau tem"
    if calcDelta(a, b, c) < 0:
        return "Essa equacao nao possui raizes, pois seu delta e negativo"
    else:
        delta = calcDelta(a, b, c)
        if delta == 0:
            return "Essa equacao possui apenas uma raiz"
        elif delta > 0:
            return "Essa equacao possui duas raizes"
#double, double, double -> double
def retornaMenorValor(a, b, c):
    "funcao que verifica qual e o menor numero entre tres, considerando numeros iguais"
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    elif a == b and a > c:
        return a, b
    elif a == c and a > b:
        return a, c
    elif b == a and b > c:
        return b, a
    elif b == c  and b > a:
        return b, c
    elif c == a  and c > b:
        return c, a
    elif c == b and c > a:
        return c, b
    else:
        return a, b, c
#double, double, double - > string
def tipoTriangulo(a, b, c):
    "funcao que verifica tipo de triangulo"
    if a == 0:
        return "nao existe triangulo com valor de um lado valendo zero"
    elif b == 0:
        return "nao existe triangulo com valor de um lado valendo zero"
    elif c == 0:
        return "nao existe triangulo com valor de um lado valendo zero"
    else:
        if a > b and a > c:
            return "Triangulo Escaleno"
        elif b > a and b > c:
            return "Triangulo Escaleno"
        elif c > a and c > a:
            return "Triangulo Escaleno"
        elif a == b and a > c:
            return "Triangulo Isosceles"
        elif a == c and a > b:
            return "Triangulo Isosceles"
        elif b == a and b > c:
            return "Triangulo Isosceles"
        elif b == c and b > a:
            return "Triangulo Isosceles"
        elif c == a and c > b:
            return "Triangulo Isosceles"
        elif c == b and c > a:
            return "Triangulo Isosceles"
        else:
            return "Triangulo Equilatero"
#int -> double
def valorCompraFruta(a):
    "Funcao que verifica o valor da compra de macas"
    if a < 12 and a > 0:
        return "O valor total da compra foi de R$ "+ str(a*0.25)+", pois foram compradas menos de 12 macas"
    elif a >= 12:
        return "O valor total da compra foi de R$ "+ str(a*0.25)+", pois foram compradas menos de 12 macas"
    else:
        return "O valor total da compra foi de R$ "+ str(a*0.0)+", pois nao foram compradas 0 macas"
#int -> string
def anoBissexto(a):
    "Funcao que verifica se o ano e bissexto"
    ano = a/4
    ano2 = a/4.0
    if ano != ano2:
        return False
    return True
#int, int, int -> string
def verificaData(dia, mes, ano):
    "Funcao que verifica se a data existe"
    if ano > 0:
        if mes > 0 and mes < 13:
            if mes == 1:
                if dia > 0 and dia < 32:
                    return "Data Valida"
                else:
                    return "Data Invalida"
            elif mes == 2:
                if anoBissexto(ano) == True:
                    if dia > 0 and dia < 30:
                        return "Data Valida"
                    else:
                        return "Data Invalida"
                elif anoBissexto(ano) == False:
                    if dia > 0 and dia < 29:
                        return "Data Valida"
                    else:
                        return "Data Invalida"
            elif mes == 3:
                if dia > 0 and dia < 32:
                    return "Data Valida"
                else:
                    return "Data Invalida"
            elif mes == 4:
                if dia > 0 and dia < 31:
                    return "Data Valida"
                else:
                    return "Data Invalida"
            elif mes == 5:
                if dia > 0 and dia < 32:
                    return "Data Valida"
                else:
                    return "Data Invalida"
            elif mes == 6:
                if dia > 0 and dia < 31:
                    return "Data Valida"
                else:
                    return "Data Invalida"
            elif mes == 7:
                if dia > 0 and dia < 32:
                    return "Data Valida"
                else:
                    return "Data Invalida"
            elif mes == 8:
                if dia > 0 and dia < 32:
                    return "Data Valida"
                else:
                    return "Data Invalida"
            elif mes == 9:
                if dia > 0 and dia < 31:
                    return "Data Valida"
                else:
                    return "Data Invalida"
            elif mes == 10:
                if dia > 0 and dia < 32:
                    return "Data Valida"
                else:
                    return "Data Invalida"
            elif mes == 11:
                if dia > 0 and dia < 31:
                    return "Data Valida"
                else:
                    return "Data Invalida"
            elif mes == 12:
                if dia > 0 and dia < 32:
                    return "Data Valida"
                else:
                    return "Data Invalida"
        else:
            return "O mes precisa ser maior que 0 e menor que 13"
    else:
        return "O ano precisa de maior que 0"
#double, double, double, double -> string
def verificaAprovacao(p1,p2,p3,nt):
    "Funcao que verifica a media final"
    media = 0
    if p1 > p2  and p2 > p3:
        media = (((p1+p2)/2)*0.8)+(0.2*nt)
        if media >= 5:
            return "Aprovado"
        else:
            return "Reprovado"
    elif p2 > p1  and p2 < p3:
        media = (((p2+p3)/2)*0.8)+(0.2*nt)
        if media >= 5:
            return "Aprovado"
        else:
            return "Reprovado"
    elif p2 < p1  and p2 > p3:
        media = (((p1+p2)/2)*0.8)+(0.2*nt)
        if media >= 5:
            return "Aprovado"
        else:
            return "Reprovado"
    elif p3 > p1  and p2 < p3:
        media = (((p2+p3)/2)*0.8)+(0.2*nt)
        if media >= 5:
            return "Aprovado"
        else:
            return "Reprovado"
    elif p3 > p2  and p2 < p1:
        media = (((p1+p3)/2)*0.8)+(0.2*nt)
        if media >= 5:
            return "Aprovado"
        else:
            return "Reprovado"
    elif p1 < p3  and p2 > p3:
        media = (((p2+p3)/2)*0.8)+(0.2*nt)
        if media >= 5:
            return "Aprovado"
        else:
            return "Reprovado"
    elif p2 > p3  and p2 > p1:
        media = (((p2+p3)/2)*0.8)+(0.2*nt)
        if media >= 5:
            return "Aprovado"
        else:
            return "Reprovado"
    elif p1 == p2  and p1 > p3:
        media = (((p1+p2)/2)*0.8)+(0.2*nt)
        if media >= 5:
            return "Aprovado"
        else:
            return "Reprovado"
    elif p1 == p2  and p1 < p3:
        media = (((p1+p3)/2)*0.8)+(0.2*nt)
        if media >= 5:
            return "Aprovado"
        else:
            return "Reprovado"
    elif p2 == p1  and p1 < p3:
        media = (((p1+p3)/2)*0.8)+(0.2*nt)
        if media >= 5:
            return "Aprovado"
        else:
            return "Reprovado"
    elif p2 == p1  and p2 > p3:
        media = (((p1+p2)/2)*0.8)+(0.2*nt)
        if media >= 5:
            return "Aprovado"
        else:
            return "Reprovado"
    elif p3 == p1  and p1 > p2:
        media = (((p1+p3)/2)*0.8)+(0.2*nt)
        if media >= 5:
            return "Aprovado"
        else:
            return "Reprovado"
    elif p3 == p2  and p1 > p3:
        media = (((p1+p2)/2)*0.8)+(0.2*nt)
        if media >= 5:
            return "Aprovado"
        else:
            return "Reprovado" 
    else:
        if p1 == p2 and p1 == p3 and p2 == p3:
            media = (((p2+p3)/2)*0.8)+(0.2*nt)
            if media < 5:
                return "Reprovado"
            else:
                return "Aprovado"
        

        
        

                
        
       

            
        
        
