# questão 1
from audioop import reverse
from re import L


def quant_palavras(frase):
    """Esta funcao recebe uma string e conta o numero de palavras nesta string
    str -> int"""
    numero_palavras = str.split(frase)
    return len(numero_palavras)

# questão 2
def contafrases(frase):
    """Esta funcao recebe uma string e conta o numero de frases nesta
    str -> int"""
    ponto = frase.count(".")
    interrogacao = frase.count("?")
    exclamacao = frase.count("!")
    reticencias = frase.count("...")
    frasecomreticencias = (reticencias*3)
    if "..." in frase:
        return (ponto+interrogacao+exclamacao+reticencias-frasecomreticencias)
    else:
        return (ponto+interrogacao+exclamacao)

# questão 3
def retira_pontuacao(frase):
    """Esta funcao recebe uma string e substitui sua pontuação por espaços
    str -> str"""
    if "." in frase:
        frase = frase.replace("."," ")
    if "!" in frase:
        frase = frase.replace("!"," ")
    if "?" in frase:
        frase = frase.replace("?"," ")
    if "..." in frase:
        frase = frase.replace("..."," ")
    if "," in frase:
        frase = frase.replace(","," ")
    if "-" in frase:
        frase = frase.replace("-"," ")
    return frase

# questão 4
def inverte(frase):
    """Essa função recebe uma frase, remove sua pontação e a inverte
    str -> str"""
    frase = retira_pontuacao(frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    return(frase)

# questão 5

def insere(lista,n):
    """Esta funcao recebe uma lista e um elemento, adiciona esse elemento na lista e a organiza
    str -> str"""
    lista.insert(0,n)
    lista.sort()
    return lista

# questão 6

def maiores(lista,n):
    """Esta funcao recebe uma lista e um numero e avalia quais numeros da lista são maiores que o numero fornecido
    list -> list"""
    l = []
    for i in range(len(lista)):
        if lista[i] > n:
            l.append(lista[i])
    l.sort()
    return l

# questão 7
def acima_da_media(notas):
    """Essa função recebe uma lista com as notas de alunos, calcula a media cria uma ordenada com as notas que ficaram acima da media
    list -> list"""
    notas_media =[]
    media = sum(notas)/len(notas)
    for i in range (len(notas)):
        if notas[i] > media:
            notas_media.append(notas[i])
    notas_media.sort()
    return notas_media