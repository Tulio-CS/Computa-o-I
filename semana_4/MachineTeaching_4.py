# Concatenacao
def concatenacao(a, b):
    """Recebe duas strings e retorna uma string
    str + str -> str"""
    return a + b + b + a

#Subistituicao
def substitui(s ,x , i):
    """Recebe uma string, uma posção na string e um caractere e substitui esse caractere em determinada posição na string
    str + int + str -> str"""
    a = list(s)
    a[i] = x
    return str.join("",a)

# Hashtag
def hashtag(s):
    """recebe uma string, encontra seu meio e coloca uma hashtag no seu inicio meio e fim
    str -> str"""
    l = len(s)
    return "#" + s[0:l//2] + "#" + s[l//2:] + "#"

# Filtragem
def filtra_pares(t):
    """recebe uma tuple e filtra seus numeros pares
    tuple -> tuple"""
    a,b,c,d = t
    l = []
    if a%2 == 0 :
        list.append(l,a)
    if b%2 == 0 :
        list.append(l,b)
    if c%2 == 0 :
        list.append(l,c)
    if d%2 == 0 :
        list.append(l,d)
    return tuple(l)

# Detecção de colisoes com tuplas
def colisao(ret1,ret2):
    """recebe duas tuplas referentes as coordenadas de dois retangulos e analisa se houve ou não uma colisão 
     tuple, tuple --> bool"""
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    if (x_sup_dir1 < x_inf_esq2 or y_sup_dir1 < y_inf_esq2 or x_sup_dir2 < x_inf_esq1 or y_sup_dir2 < y_inf_esq1 ):
        return False
    else:
        return True








