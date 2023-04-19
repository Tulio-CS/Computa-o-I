from random import randint

# Funçoes extra
def dados():
    """Esta função roda um dado com Xn de faces um numero Yn de vezes e retorna seus valores
    input -> list"""
    lista = []
    x = input("Qual o numero de faces do dado\n")
    y = input("Quantas vezes o dado sera rolado\n")
    for i in range(int(y)):
        lista.append(randint(1,int(x)))
    print(lista)
    return lista
# Questão 1
def sequencia(lista):
    """Esta função recebe uma lista com os valores do rolamento de um dado e conta o numero de vezes que os dados se repetem
    list -> int"""
    contador = 0
    consecutivos = 0
    for i in range(len(lista)-1):
        j = i+1
        if lista[i] == lista[j]:
            consecutivos += 1
        elif lista[i] != lista[j] and consecutivos != 0:
            consecutivos = 0
            contador += 1
    if consecutivos != 0:
        contador += 1        
    return contador
sequencia(dados())
#Questão 2
def questao2(i,a,b,c):
    if a >= b:
        return ("Erro, B não pode ser menor do que A")
    else:
        if i == 1:
            return (((a+b)*c)/2),("i={}, a={}, b={}, c={}".format(i,a,b,c))
        if i == 2:
            return (a*a , b*b , c*c,"i={}, a={}, b={}, c={}".format(i,a,b,c))
        if i == 3:
            return ((a+b+c)/3,("i={}, a={}, b={}, c={}".format(i,a,b,c)))
        if i == 4:
            l = 0
            for i in range(a,b+1,c):
                l += i
            return l,("i={}, a={}, b={}, c={}".format(i,a,b,c))

print(questao2(1,2,3,4))
    

    
# Questão 3
def busca():
    """Essa funcao recebe uma matriz e um setor de uma empresa e retorna os contatos na matriz que participam deste setor
    str , list -> list"""
    matriz = []
    resultado_busca = []
    x = input("Você quer digitar elemento por elemento ou entregar a matriz inteira?\n1 = elemento por elemento\n2 = Matriz completa\n")
    if x == str(2):
        y = input("Digite a matriz\n")
        y = y.replace(" ","")
        y = y.split(",")
        for i in range(0,len(y),4):
            matriz.append(y[i:i+4])
    elif x == str(1):
        continuar = 1
        while continuar == 1:
            nome = input("Qual o nome do funcionario\n")
            registro = input("Qual o registro do funcionario\n")
            setor = input("Qual o setor do funcionario?\n")
            telefone = input("Qual o telefone do funcionario?\n")
            funcionario = [nome,registro,setor,telefone]
            matriz.append(funcionario)
            y = input("Você quer adicionar outro funcionario?\n1 = Sim\n2 = Não\n")
            if y == str(2):
                continuar = 0
    z = input("Qual o setor que a busca será realizada\n")
    for i in range (len(matriz)):
        if z in matriz[i]:
            matriz[i].pop(2)
            resultado_busca.append(matriz[i])
    return resultado_busca
#print(busca())


