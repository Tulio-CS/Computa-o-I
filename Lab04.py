# Questão 1

def siga(t):
    """recebe uma tupla com um nome e tres notas e retorna o nome a media e a situação do aluno
    tuple(str,int,int,int) -> tuple(str,int,str)"""
    a,b,c,d = t 
    if (b+c+d)/3 >= 7:
        return ((a  , (int((b+c+d)/3)) ,  "aprovado , parabéns!"))
    elif 5 <= (b+c+d)/3 < 7:
        return ((a , (int((b+c+d)/3)) , "aprovado"))
    else:
        return ((a , (int((b+c+d)/3)) , "reprovado"))

# Questão 2

def zodiaco(ano):
    """Recebe um ano e divide seu valor por 12, o resto da divisão corresponde ao seu ano no zodiaco
    int -> str"""
    l = ["macaco","galo","cão","porco","rato","boi","tigre","coelho","dragao","serpente","cavalo","carneiro"]
    return l[ano%12]

# Questão 3

def numero(numero):
    """Recebe uma string uma string e analisa se tamanho, se compativel retorna uma tuple com o DDD e o numero de telefone
    str -> tuple(str,str)"""
    l = list(numero)
    if len(l) == 8 :
        return (("",numero))
    elif len(l) == 9:
        return (("",numero))
    elif len(l) == 10:
        return ((numero[:2],numero[2:]))
    elif len(l) == 11:
        return ((numero[:2],numero[2:]))
    else:
        return (("",""))

# Questão 4
def formato_data(data):
    """Esta função recebe uma string de 8 elementos referentes a alguma data qualquer e retorna os formato possivel para determinada data
    str -> tuple"""
    l = []
    if 1 <= int(data[0:2]) <= 31 and 1 <= int(data[3:5]) <= 12 :
        list.append (l,"dd/mm/yy")
    if 1 <= int(data[0:2]) <= 12 and 1 <= int(data[3:5]) <=31 :
        list.append (l,"mm/dd/yy")
    if 1 <= int(data[3:5]) <= 12 and 1 <= int(data[6:]) <= 31 :
        list.append (l,"yy/mm/dd")
    return tuple(l)


