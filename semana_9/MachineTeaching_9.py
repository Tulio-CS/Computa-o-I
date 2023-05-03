# eh_quadrada
def eh_quadrada(matriz):
    """Essa função analiza se uma matriz e quadrada 
    list -> bool"""
    if len(matriz) == 0:
        return True
    for i in range(len(matriz)):
        while i < len(matriz):
            if len(matriz[i]) == len(matriz):
                i += 1
            else:
                return False
        return True

#Conta numero
def conta_numero(numero,matriz):
    """Essa funcao recebe uma matriz e conta o numero de ocorrencias do numero na matriz
    int , list -> int"""
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                contador += 1
    return contador

#Media matriz
def media_matriz(matriz):
    """Essa função recebe uma matriz e retorna a media da mesma
    list -> int"""
    soma_matriz = 0
    numero_elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma_matriz += matriz[i][j]
            numero_elementos += 1
    return round(soma_matriz/numero_elementos,2)

#Melhor volta
def melhor_volta(matriz):
    """Essa função recebe uma lista com os tempos de voltas de kart e retorna uma tupla com o melhor corredor seu melhor tempo e a volta com o melhor tempo
    list -> tuple"""
    melhor = []
    for i in range(len(matriz)):
        melhor.append(min(matriz[i]))
    melhor_corredor = melhor.index(min(melhor))+1
    n_volta = (matriz[melhor.index(min(melhor))].index(min(melhor)))+1
    return (melhor_corredor,min(melhor),n_volta)

#busca
def busca(setor,matriz):
    """Essa funcao recebe uma matriz e um setor de uma empresa e retorna os contatos na matriz que participam deste setor
    str , list -> list"""
    resultado_busca = []
    for i in range (len(matriz)):
        if setor in matriz[i]:
            matriz[i].pop(2)
            resultado_busca.append(matriz[i])
    return resultado_busca



