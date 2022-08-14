# questão 1


#a
def adiciona_contato(nome, telefone = "", email = "", instagram  = ""):
    """Cria um contato com as informaçoes fornecidas pelo usuario
    str, str, str, str - list"""
    if nome ==  "":
        return "Um nome precisa ser atribuido para criar um contato"
    elif type(telefone) == list or type(telefone) == tuple:  
        return "Apenas um telefone pode ser adicionado ao criar um contato"    
    else:
        return [nome, [telefone], email, instagram]

#b
def atualizar_contato(contato, atributo, informacao):
    """Altera os valores de uma lista predeterminada se todos suas exigencias forem cumpridas
    int, int, list -> list"""
    if atributo >= len(contato) :
        return False 
    if atributo == 1 and informacao == contato[1][0]:
        return False
    if atributo == 1 and informacao != contato[1][0]:
        contato[1].insert(1,informacao)
        return True
    else:
        contato[atributo] = informacao
    return True 




# questão 2

def aminoacido(rna):
    """Recebe uma string de com 9 elementos referentes a trinca de RNA,  analisa os analisa de 3 e retorna o aminiacido respectivo
    str -> str"""
    trinca = {"UUU":"Phe","CUU":"Leu","UUA":"Leu","AAG":"Lisina","UCU":"ser","UAU":"Tyr","CAA":"Gln"}
    return str.join("-",(trinca[str.upper(rna[0:3])] , trinca[str.upper(rna[3:6])], trinca[str.upper(rna[6:])]))

print(aminoacido("uuucuucaa"))