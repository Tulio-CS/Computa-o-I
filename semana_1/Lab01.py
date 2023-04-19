
""" Questão 1 """
def area_retangulo(base,altura):
    """multiplica a base pela altura e retorna o valor da área do retângulo"""
    return (base*altura)

""" Questão 2 """
def superficie_cubo(c):
    """Calcula a area do quadrado(c**2) e multiplica pelo seu numero de lados (6)"""
    return 6*(c**2)

""" Questão 3 """
def pi():
    """define um valor para pi"""
    return(3.14159)

def area_circulo(r):
    """calcula a área de um circulo qualquer a partir de seu raio(r)"""
    return (pi()*r**2)

def coroa(r1,r2):
    """calcula o problema da coroa circular subtraindo a área do circulo menor (r2) da área do circulo maior (r1)"""
    return(area_circulo(r1)- area_circulo(r2))

""" Questão 4 """
def media(v1,v2):
    """calcula a media de dois valores quaisquer somando o valor 1(v1) com o valor 2 (v2) e dividindo por 2"""
    return ((v1+v2)/2)

""" Questão 5 """
def ordenada(a,b,c,x):
    """Calcula a ordenada de uma função de segundo grau dado os valores de A(ax**2) B(bx) e C(c) e o valor de X"""
    return (a*x**2+b*x+c)

""" Questão 6 """
def media_ponderada(x,peso_de_x,y,peso_de_y):
    """Calcula a media ponderada de dois numeros(x,y) considerando seus respectivos pesos"""
    return ((x*peso_de_x)+(y*peso_de_y))/(peso_de_x+peso_de_y)

""" Questão 7 """
def soma_infinita(q):
    """Calcula a soma dos termos de uma PG"""
    return (1 / (1 - q))

def primeiros_termos(q,n):
    """Calcula a soma dos (n) primeiros termos de uma PG"""
    return (1*(q**n-1)/(q-1))

def erro_pg(q,n):
    """Subtrai a soma dos primeiros termos de uma PG da soma dos termos dessa PG, calculando o erro entre os valores"""
    return (soma_infinita(q))-(primeiros_termos(q,n))

""" Questão 8 """
def valor_conta(valor_conta):
    """Calcula o valor da conta do restaurante considerando uma gorjeta de 15%"""
    return (valor_conta+(valor_conta*0.15))

""" Questão 9 """
def gorjeta(valor_conta,taxa=0.1):
    """Calcula o valor da gorjeta a partir do valor da conta considerando uma taxa de 10%, o úsuario devera usar a notação 0.1 para calcular corretamente a gorjeta"""
    return valor_conta*taxa

""" Questão 10 """
def saldo_final(saldo_inicial,numero_de_meses,taxa_juros_mensal):
    """calcula o saldo final de uma conta de juros simples, o úsuario devera usar a notação 0.n sendo n o juros mensal"""
    return (saldo_inicial*(1+(taxa_juros_mensal*numero_de_meses)))

""" Questão 11 """
def distancia_correnteza_barco(velocidade_da_correnteza,largura_rio,velocidade_barco_perpendicular_correnteza):
    """calcula a distancia que a correnteza arrasta um barco considerando a largura do rio, velocidade do barco e velocidade da correnteza"""
    return velocidade_da_correnteza*(largura_rio/velocidade_barco_perpendicular_correnteza)


print(superficie_cubo(5))