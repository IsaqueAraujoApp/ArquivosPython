def MaioresNaListta(lista, n):
    listaresultante = []
    if n in lista:
        lista.sort()
        index = lista.index(n)
        listaresultante = lista[index+1:]
        return listaresultante
    else:
        lista.append(n)
        lista.sort()
        index = lista.index(n)
        listaresultante = lista[index+1:]
        return listaresultante
def RetornaSegundoMaior(lista):
    indice = lista.index(max(lista))
    lista[indice] = 0
    return lista.index(max(lista))
def Media(lista):
    media = sum(lista)/((len(lista))*1.0)
    listarresultante = []
    lista.append(media)
    lista.sort()
    index = lista.index(media)
    listaresultante = lista[index+1:]
    if media in listaresultante:
        listaresultante.reverse()
        index2 = listaresultante.index(media)
        listaresultante = listaresultante[index2-1::-1]
        return media, listaresultante
    else:
        return media, listaresultante
def ListaParListaImpar(lista):
    listapar = []
    listaimpar = []
    if lista[0]%2==0:
        listapar.append(lista[0])
    else:
        listaimpar.append(lista[0])
    if lista[1]%2==0:
        listapar.append(lista[1])
    else:
        listaimpar.append(lista[1])
    if lista[2]%2==0:
        listapar.append(lista[2])
    else:
        listaimpar.append(lista[2])
    if lista[3]%2==0:
        listapar.append(lista[3])
    else:
        listaimpar.append(lista[3])
    return listapar, listaimpar
def notas(p):
    n100 = p/100
    n50 = (p%100)/50
    return n100+n50
    
