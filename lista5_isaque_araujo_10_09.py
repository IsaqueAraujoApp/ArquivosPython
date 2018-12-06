#string -> string
def ContrarioUpper(s):
    "Inverte a String e tudo vira CAPS"
    return str.upper(s[::-1])
#string -> string and int
def QuantVogal(s):
    "Conta a quantidade de cada vogal que tem em uma string"
    a = str.count(s,"a")
    e = str.count(s,"e")
    i = str.count(s,"i")
    o = str.count(s,"o")
    u = str.count(s,"u")
    tupla = "a = "+str(a), "e = "+str(e), "i = "+str(i), "o = "+str(o), "u = "+str(u)
    return tupla
#string, string -> int
def IndiceLetra(string, caracter):
    "Retorna o segundo indice da letra escolhida na palavra"
    indice = str.index(string,caracter)
    if str.count(string, caracter) < 2:
        return "A quantidade do caracter escolhido na string e menor que 2"    
    return str.index(string, caracter, indice+1)
#string -> int
def NumerosPalavras(frase):
     "Conta a quantiade de palavras que tem na frase"
     separador = str.split(frase)
     return len(separador)
##revisar
#tupla -> tupla
def TuplaResultante(a,b):
    "Recebe duas tuplas e cria uma nova com o primeiro indice da maior e o ultimo da menor"
    if len(a)> len(b):
        return a[0],b[-1]
    elif len(b)> len(a):
        return b[0],a[-1:]
#string -> string
def JogoVelhaNoBranco(frase):
    "Insere o jogo da velha em todo espaco em branco que tem na frase"
    separador = str.split(frase," ")
    return str.join("#", separador)
#lista, lista -> lista int
#return L1[0],L2[0],L1[1],L2[1],L1[2],L2[2]
def UneLista(L1,L2):
    "Cria uma lista nova com base em duas concatenando suas posicoes"
    lista = []
    i = 0
    while i < 3:
        lista.append(L1[i])
        lista.append(L2[i])
        i+=1
    return lista
#lista, lista -> lista string int
def UneListaNomesNotas(L1,L2):
    "Cria uma lista com 3 tuplas, cada tupla tem dois elementos sendo um o nome e outro a nota"
    lista = []
    i = 0
    tupla = L1[0],L2[0],L1[1],L2[1],L1[2],L2[2]
    while i < len(tupla):
        lista.append(tupla[i:i+2])
        i+=2
    return lista
#int, int -> list int
def listaReturn(n, m):
    "Retorna uma lista de numeros em ordem crescente comecando em 1, caso o numero m esteja na lista, o numero e multiplicado por dois gerando uma nova lista"
    lista = []
    if m > n:
        lista = range(1,n+1)
    else:
        lista = range(1,n+1)
        lista[m-1] = (lista[m-1])*2        
    return lista


        

    
    
