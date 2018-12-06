#string -> string
def posicaoImpar(s):
    "Funcao que retorna os caracteres das posicoes impares de um string"
    return s[1:len(s)+1:2]
#string -> string
def letraMeio(s):
    "Funcao que retorna os caracteres do meio de uma string"
    if len(s)% 2 != 0:
        return s[len(s)/2:len(s)/2+1]
    return s[len(s)/2-1:len(s)/2+1]
#string, string -> string
def PartePrimeiraMaisParteSegunda(s1, s2):
    "Funcao que retorna parte que corta o inicio de uma string e o fim de outra e depois junta as palavras"
    if len(s1) < 5 or len(s2) < 5:
        return "As duas Strings devem possuir pelo menos 5 caracteres"
    return s1[2:len(s1)] + s2[0:len(s2)-2]
#string, string, int -> string
def SubstituirLetra(palavra, letra, posicao):
    "Funcao que substitui uma letra da string em uma certa posicao"
    part1 = palavra[0: posicao]
    part2 = palavra[posicao+1:len(palavra)]
    return part1+letra+part2
#string -> string
def MeioString(s):
    "Funcao que retorna o meio de uma string"
    part1 = s[0:len(s)/2]*2
    part2 = s[len(s)/2:len(s)]*2
    return part1+part2
#string -> string
def InsereJogoDaVelha(s):
    "Funcao que insere o jogo da velha em tres posicoes da string"
    part1 = s[0:len(s)/2]
    part2 = s[len(s)/2:len(s)]
    return "#"+part1+"#"+part2+"#"
#string -> string
def RotacionaString3(s):
    "Funcao que rotaciona uma string"
    part1 = s[0:3]
    part2 = s[3:len(s)]
    return part2+part1
#string -> string
def RotacionaStringX(s, numberx):
    "Funcao que rotaciona uma string"
    part1 = s[0: numberx]
    part2 = s[numberx:len(s)]
    return part2+part1
#string, string -> string
def TotalDias(data1, data2):
    "Funcao que retorna a quantidade de dias passados entre duas datas"
    dia1 = int(data1[0:2])
    mes1 = int(data1[3:5])
    ano1 = int(data1[6:10])
    dia2 = int(data2[0:2])
    mes2 = int(data2[3:5])
    ano2 = int(data2[6:10])
    diasSemMes = (30-dia1) + dia2
    diasComMes = (12-mes1)*30+(12 -(12-mes2+1))*30
    diasComMesComAnos = (ano2-ano1-1)*12*30
    return "O total de dias e " + str(diasSemMes+diasComMes+diasComMesComAnos)

