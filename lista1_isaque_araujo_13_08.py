#Exe 1
#float, float -> float
def RetanguloArea(Vbase, Valtura):
    "Funcao que calcula a area de um retangulo"
    return Vbase*Valtura
#Exe 2
#int, int -> int
def ValorDivisaoEResto(n1,n2):
    "Funcao que calcula o valor da divisao e retorna seu resto"
    return n1/n2, n1%n2
#Exe 3
#float, float, float, float -> float
def OrdenadaFuncaoSegGrau(a,b,c, abscissa):
    "Calcula o valor da ordenada de uma funcao do 2 grau, ou seja, valor do Y"
    return (a*abscissa**2)+b*abscissa+c
#Exe 4
#float -> float
def GorjetaDoGarcom(ValorConta):
    "Calcula o valor da gorjeta(dez por cento) do garcom baseado no valor da conta."
    return ValorConta*0.1
#Exe 5
#float, float -> float
def MediaEntreDoisNumeros(n1,n2):
    "Calcula a media entre dois numeros"
    return (n1+n2)/2.0
#Exe 6
#float, float, float, float -> float
def MediaPonderadaEntreDoisNumeros(n1,n2,p1,p2):
    "Calcula a media ponderada entre dois numeros com seus respectivos pesos"
    return (n1*p1+n2*p2)/(p1+p2)
#Exe 7
#float, float -> float
def AreaDaCoroaAnel(r1,r2):
    "Calcula a area da coroa do anel, ou seja, calcula a area do circulo maior e subtrai a area do circulo menor"
    return (3.14*r1**2)-(3.14*r2**2)
#Exe 8
#float, float, float -> float
def DistanciaArrastoDoBarco(Vcorrenteza, Lrio, Vbarco):
    "Calcula a distancia em que o barco foi arrastado devido a velocidade da correnteza"
    return Vcorrenteza*(Lrio/Vbarco)
#Exe 9
def SaldoFinalConta(SaldoInicial, meses, taxa):
    "Calcula o valor final da conta baseado em juros simples"
    return(SaldoInicial*(1 + meses*taxa))
#Exe 10
#float -> float
def erroPG(q):
    "Calcula o erro entre  valor da soma de uma PG infinita a partir de 1.0 e a soma dos n primeiros termos dessa PG"
    return 1 / (1 - q) - (1 + q + q * q)  
#Exe 11
#float, float -> float
def GorjetaEValorTotalPorPessoa(ValorConta, nPessoas):
    "Calcula o valor da gorjeta e o valor que cada pessoa da mesa deve pagar, incluindo a parcela da gorjeta"
    return ValorConta*0.1, (ValorConta+(ValorConta*0.1))/nPessoas
#Exe 12
#float -> float
def AreaSuperficieCubo(ValorAresta):
    "Calcula a area da superficie de um cubo baseado no valor da aresta"
    return 6*(ValorAresta**2)

