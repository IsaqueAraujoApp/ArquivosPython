def corrigeplaca(placa):
    if placa[0] in "0123456789":
        return placa
    if placa[0] == "@":
        return "A" + corrigeplaca(placa[1:])
    if placa[0] == "#":
        return "T" + corrigeplaca(placa[1:])
    return placa[0]+ corrigeplaca(placa[1:])
def ler_multas():
    arqmultas = open('multamaio.txt', 'r')
    arqoutros = open('multascanceladas','w')
    lmultas = []
    dicionario = {}
    for i in arqmultas:
        sublist = i.split(",")
        dia = int(sublist[0])
        placa = sublist[1]
        velocidade = int(sublist[2])
        placa = corrigeplaca(placa)
        if velocidade <= 99:
            arqoutros.write('%d,%s,%d\n' %(dia, placa, velocidade))
        else:
            if dia not in dicionario:
                dicionario[dia] = [placa,velocidade]
            else:
                dicionario[dia] += [placa,velocidade]
    for j in dicionario:
        if j not in lmultas:
            if len(dicionario[j]) == 2:
                lmultas.append([j,dicionario[j]])
            else:
                k = 0
                p = 0
                while p < (len(dicionario[j])/2):
                    valor = dicionario[j]
                    if k == 0:
                        lmultas.append([j])
                        indice = lmultas.index([j])
                        lmultas[indice].append(valor[k:k+2])
                    else:
                        lmultas[indice].append(valor[k:k+2])
                    k+=2
                    p+=1
    arqmultas.close()
    arqoutros.close()
    return lmultas
def DiasComMaioresQuantidadesdeMultas():
    x = ler_multas()
    maiores = []
    j = 0
    while j < 3:
        salvo = 0
        indice = 0
        k = 0
        for i in x:
            if len(i)> salvo:
                salvo = len(i)
                k+=1
        maiores.append(x[k])
        x.pop(k)
        j+=1
    return maiores

        
        
    
        
