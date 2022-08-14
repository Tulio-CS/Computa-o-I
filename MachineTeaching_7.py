# Filtramultiplos

def filtraMultiplos(lista,n):
    """essa funcao recebe uma lista e um numero e filtra na lista os numeros que sao divisiveis por n
    list -> list"""
    multiplos = []
    for i in range(len(lista)):
        if lista[i]%n == 0:
            multiplos.append(lista[i])
    return (multiplos)


# consoantes em maiusculas
def uppCons(frase):
    """Esta função recebe uma string e torna as consoantes maiusculas
    str -> str"""
    frase = list(frase)
    for i in range(len(frase)):
        if frase[i] in "BCDFGHJKLMNPQRSTVWXYZÇbcdfghjklmnpqrstvwxyzç":
            frase[i] = frase[i].upper()
    frase = "".join(frase)
    return frase

# pos letra
def posLetra(string,letra,ocorrencia):
    string = list(string)
    ocorrencias = []
    i = 0 
    while i < len(string):
        if string[i] == letra:
            ocorrencias.append(i)
            i += 1
        i += 1
    if ocorrencia <= (len(ocorrencias)):
        ocorrencia = ocorrencia-1
        ocorrencias[ocorrencia]
        return ocorrencias[ocorrencia]
    else:
        return -1

    
# repetidos
def repetidos(lista):
    """Essa função recebe uma lista de numeros e conta quantas vezes numeros consecutivos se repetem
    list ->int"""
    contador = 0
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            contador += 1
    return contador

# fatorial
def fatorial(numero):
    '''essa função calcula o fatorial de um determinado numero
    int -> int'''
    multiplicacao = 1
    for i in range(1, (numero+1)):
        multiplicacao = multiplicacao * i  
    return multiplicacao

# peça perdida

def faltante(lista):
    """Essa funcao recebe uma lista com a numeração de peças e retorna qual peça esta faltando
    list -> int"""
    faltando = []
    for i in range(1,len(lista)+2):
        if i not in lista:
            faltando.append(i)
    return faltando[0]


