#intercala

def intercala(l1,l2):
    """Fatia as listas e as organiza de forma a intercalar l1 e l2
    list + list -> list"""
    l3 = l1 + l2
    l3[::2] = l1
    l3[1::2] = l2
    return l3

# pontos por time

def pontos_por_time(l):
    """recebe uma lista com o numero de gols de dois times em dois jogos e analisa a quantidade de pontos que cada time fez
    list -> dict""" 
    p1 = []
    p2 =[]
    if l[0][2][0] > l[0][2][1]:
        list.append(p1,3)
    if l[0][2][0] < l[0][2][1]:
        list.append(p2,3)
    if l[0][2][0] == l[0][2][1]:
        list.append(p1,1)
        list.append(p2,1)
    if l[1][2][0] > l[1][2][1]:
        list.append(p2,3)
    if l[1][2][0] < l[1][2][1]:
        list.append(p1,3)
    if l[1][2][0] == l[1][2][1]:
        list.append(p1,1)
        list.append(p2,1)
    return {l[0][0]:sum(p1),l[0][1]:sum(p2)}

# Colchão 
def colchao(col, h, l):
    """recebe as dimensoes do colchão e da porta e avalia se o colchao passa pela porta
    list + int + int -> bool"""
    if col[1] <= h or col[1] <= l:
        return True
    elif col[2] <= h or col[2]<= l:
        return True
    else:
        return False

