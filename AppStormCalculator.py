def porcentagemClassificacao():
    lista = valores()
    total = input("Digite o total de classificacoes:")
    print total
    if sum(lista) != total:
        print "A soma de classicaoes nao e igual ao numero total. Digite os valores novamente:"
        return porcentagemClassificacao()
    j = 0
    while j < 5:
        print "Quantidade de " + str(j+1)+ " estrelas: "+ str(lista[j])+ " porcentagem entre o total: " + str(lista[j]/(total*1.0))
        j+=1
def valores():
    i = 1
    lista = []
    while i <= 5:
        x = input("Digite a quantidade de "+ str(i)+ " estrela:")
        lista.append(x)
        i+=1
    return lista
    
    
        
        
