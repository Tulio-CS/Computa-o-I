
# frequencia de palavras
def freq_palavras(texto):
    """Essa função recebe um texto e analisa a frequencia com que as palavras se repetem
    str -> dict"""
    frequencia = {}
    texto = texto.split()
    for i in range(len(texto)):
        if texto[i] in frequencia:
            frequencia[texto[i]] += 1
        if texto[i] not in frequencia:
            frequencia[texto[i]] = 1
    return frequencia
print(freq_palavras("jhulia eu eu legal"))
# Total
def total(lista,tabela):
    """Esta função recebe uma lista de itens e uma tabela de precos referentes aos itens e soma os valores
    list -> int"""
    lista = list(lista)
    total = 0
    for i in range(len(lista)):
        total = total + (tabela[lista[i]])
    return round(total,2)

# Lingia_p
def lingua_p(palavra):
    """Esta função recebe uma palavra e a traduz para a lingua P
    str -> str"""
    palavra = palavra.lower()
    palavra = list(palavra)
    traducao = []
    j = 0
    for i in range(len(palavra)):
        if palavra[i] in "aeiouãéáú":
            traducao.insert(j,palavra[i])
            traducao.insert(j+1,"p")
            traducao.insert(j+2,palavra[i])
            j += 3
        else:
            traducao.insert(j,palavra[i])
            j += 1
    traducao = "".join(traducao)
    return traducao

# Qtd de divisores
def qtd_divisores(numero):
    """Esta função recebe um numero e calcula seu numero de divisores
    int -> int"""
    qtd = []
    for i in range(1,numero+1):
        if numero%i == 0:
            qtd.append(i)
    return len(qtd)

# Primo
def primo(numero):
    """Essa função recebe um numero e avalia se ele e um numero primo ou não
    int -> bool"""
    qt_div = []
    for i in range(1,numero+1):
        if numero%i == 0:
            qt_div.append(i)
    if len(qt_div) <= 2:
        return True
    else: 
        return False

# Soma H
def soma_h(numero):
    """Essa função recebe um numero e retorna a soma da divisão de 1 por h, h vezes
    int -> int"""
    h = 0
    for i in range(1,numero+1):
        h += 1/i
    return round(h,2)












