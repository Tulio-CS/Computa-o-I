# questão 1
"""calcula o valor absoluto de um numero qualquer
complex -> float"""

def valor_absoluto(valor):
    if valor<0:
        return(-valor)
    else:   
        return(valor)

# questão 2

def delta(a, b, c):
    """ Calcula o delta de um polinomio de segundo grau
    int, int, int -> float"""
    return b**2 - 4 * a * c

def num_raizes(a ,b, c):
    """analisa o valor de delta e retorna uma string que diz o numero de raizes reais da equação
    int, int, int -> str"""

    if delta(a, b, c) < 0:
        return "A equação não tem raizes reais"
    else:
        if  delta(a,b, c) == 0:
            return "A equação tem uma raiz real"
        else:
            if delta(a, b, c) > 0:
                return "A equação tem duas raizes reais"

# questão 3
"""Recebe um texto e o copia um numero "n" de vezes
int, str -> str """
def aniversario(n,texto):
    return n * texto

# questão 4
def data(dia, mes, ano):
    return str(dia) + "/" + str(mes) + "/" + str(ano)

# questão 5
"""Calcula o valor de f(x) para para a função matematica da questão 5 do Laboratorio de computação 1 numero 3
float -> float"""
def funcao(x):
    if x<0:
        return 0
    else:
        if x <=2:
            return(x)
        else:
            if 2 < x <= 3.5:
                return(2)
            else:
                if 3.5 < x <= 5:
                    return(3)
                else:
                    return(x ** 2 - 10 * x + 28)
                    
# questão 6

# letra a
"""Calcula o valor do desconto do INSS levando em conta o salario bruto e os impostos progressivos
int -> float"""
def inss(salario_bruto):
    if salario_bruto <= 2000:
        return salario_bruto * 6 / 100 
    else:
        if salario_bruto <= 3000:
            return salario_bruto * 8 / 100 
        else:
            return salario_bruto * 10 / 100

# letra b
"""Calcula o valor do desconto do Imposto de Renda levando em conta a tabela fornecida na questão
int -> float"""
def ir(salario_bruto):
    if salario_bruto <= 2500:
        return salario_bruto * 11 / 100 
    else:
        if salario_bruto <= 5000:
            return salario_bruto * 15 / 100
        else:
            return salario_bruto * 22 / 100

# letra c
"""Calcula o subtrai o INSS e o IR do salario bruto, retornando o salario liquido
int -> float"""
def salario_liquido(salario_bruto):
    return salario_bruto - inss(salario_bruto) - ir(salario_bruto)