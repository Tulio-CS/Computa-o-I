# Questão 1

def apagatelefone(listadecontato,telefone):
    """Esta função recebe um contato e um telefone, se o telefone esta salvo no contato, esse e removido, caso contrario nada acontece
    list, str -> bool"""
    if telefone in listadecontato[1]:
        listadecontato[1].remove(telefone)
        return True
    else:
        return False

# Questão 2

def campeonato(tabelapontos):
    pontos = []
    ordemclassificacao = []
    nomes = []
    # faz uma lista com apenas os pontos de cada time
    for j in range(len(tabelapontos)):
        pontos.append(tabelapontos[j][1])
    saldo = max(pontos)
    # coloca os times em ordem crescente de pontos
    for i in range(saldo+1):
        for j in range(len(tabelapontos)):
            if tabelapontos[j][1] == i:
                ordemclassificacao.append(tabelapontos[j])
    # faz uma lista com os nomes dos times que jogaram
    for n in range(len(tabelapontos)):
        nomes.append(tabelapontos[n][0])
    # calcula a media de pontos do campeonato
    media = sum(pontos)/len(pontos)
    campeao = ordemclassificacao[len(ordemclassificacao)-1]
    return print ("Estes foram os times que jogaram o campeonato {}".format(", ".join(nomes))),"\n", print("O campeao foi {} com {} pontos!".format(campeao[0],campeao[1])),"\n", print("a media de pontos do campeonato foi {}".format(media)), #print([nomes,campeao[1],media])
campeonato([["botafogo",3],["galao da massa",10],["flamengo",2]])
# quetão 2 (dicionarios)

def time(tabela):
    """Esta função recebe um dicionario e filtra o time com o maior numero de pontos, calcula a media de pontos e a lista dos times que jogaram
    dict->tuple"""
    time_campeao = max(tabela)
    media = sum(tabela.values())/len(tabela)
    times = tabela.keys()
    return(times,time_campeao,media)

# questão 3

def inseretelefone(listatelefone,telefone):
    listatelefone.insert(0,telefone)
    listaalfabetica = sorted(listatelefone)
    return listaalfabetica


