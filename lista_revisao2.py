def DivisorSubstituido(n):
    lista = []
    for valor in range(1,n+1):
        if n%valor != 0:
            lista.append("x")
        else:
            lista.append(valor)
    return lista
def ListaSemRepeticao(lista):
    listaresultante = []
    for i in lista:
        if i not in listaresultante:
            listaresultante.append(i)
    return listaresultante
def ParcelaMinima(n):
    count = 0
    soma = 0
    while n > soma:
        count+=1
        soma +=(count**2+1.0)/(count+3.0)
    return count
def JogaVelha(matriz):
    resultante = []
    i = 0
    diagonal = 0
    j = 0
    for posicao in matriz:
        if posicao[0] == posicao[1] == posicao[2]:
            return "Jogador " + posicao[0]+ " ganhou"
    while i < len(matriz):
        for posicao in matriz:
            resultante.append(posicao[i])
        if resultante[0] == resultante[1] == resultante[2]:
            return "Jogador " + resultante[0]+ " ganhou"
        resultante = []
        i+=1
    resultante = []
    while diagonal < 2:
        resultante = []
        for posicao in matriz:
            if diagonal == 0:
                resultante.append(posicao[j])
                j+=1
            elif diagonal == 1:
                resultante.append(posicao[j])
                j-=1
        if resultante[0] == resultante[1] == resultante[2]:
            return "Jogador " + resultante[0]+ " ganhou"
        diagonal+=1
        j = 2
    return "Deu Velha!"
def matriz(x,y):
    linhas = []
    colunas = []
    for i in range(1,x+1):
        colunas = []
        for j in range(1,y+1):
            colunas.append((i+1)*j)
        linhas.append(colunas)
    return linhas
def DicionarioQuadrado(lista):
    d = {}
    for valor in lista:
        d[valor]=valor**2
    return d
def VideoGame():
    count = 1
    Jogador1 = raw_input("Digite o nome do jogador 1:")
    Jogador2 = raw_input("Digite o nome do jogador 2:")
    placar = raw_input("Digite o placar da partida "+str(count)+ " seguinte modelo jogador1Xjogador2:")
    goljogador1 = 0
    goljogador2 = 0
    jogador1venceu = 0
    jogador2venceu = 0
    while True:
        valor = placar.split("X")
        goljogador1+= int(valor[0])
        goljogador2+= int(valor[1])
        if goljogador1 > goljogador2:
            jogador1venceu+=1
        elif goljogador2 > goljogador1:
            jogador2venceu+=1
        if goljogador1 - goljogador2 >= 10:
            return Jogador1+ " ganhou"
        elif goljogador2 - goljogador1 >= 10:
            return Jogador2+ " ganhou"
        if jogador1venceu >= 5:
            return Jogador1+ " ganhou"
        elif jogador2venceu >= 5:
            return Jogador2+ " ganhou"
        else:
            placar = raw_input("Digite o placar da partida "+str(count)+ " seguinte modelo jogador1Xjogador2:")

            

            
        
        

            
    
    
    
        

        
    
        
            
