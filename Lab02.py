import math
import cmath

# questão 1

# letra B
def media(a, b, c):
    """Calcula a media dos valores (a, b, c)
    int, int, int, -> float"""
    return ((a + b + c) / 3)

# letra c
def diferenca(a, b, c):
    """ Subtrai a media do maior valor de (a, b, c)
    int, int, int -> float"""
    return max(a, b, c) - media(a, b, c)

# letra d
def soma_media(a, b, c):
    """Calcula a media dos valores (a, b, c) e soma com o menor valor de (a, b, c)
    int, int, it -> float"""
    return media(a, b, c) + min(a ,b, c)

# questão 2

# letra a
def delta(a, b, c):
    """ Calcula o delta de um polinomio de segundo grau
    int, int, int -> float"""
    return b**2 - 4 * a * c

# letra b
def raiz_1(a, b, c):
    """Calcula a primeira raiz de um polinomio de segundo grau
    int, int, int -> float"""
    return (- b + cmath.sqrt(delta (a, b, c))) / (2 * a)

# letra c 
def raiz_2(a, b, c):
    """Calcula a segunda raiz de um polinomio de segundo grau
    int, int, int -> float"""
    return (- b - cmath.sqrt(delta (a, b, c))) / (2 * a)

# questão 3

# letra b
def numero_termos (a1 , an , r):
    """calcula o numero dos termos de determinada pa
    int, int, int -> float"""
    return (an - a1) / r + 1

# letra c
def soma_pa (a1 , an , r ):
    """calcula a soma da pa dado o primeiro, o ultimo termo e a razão
    int, int, int -> float"""
    return ((a1 + an) * numero_termos(a1 , an , r)) / 2

# questão 4

# letra a
def distancia(x1 , x2, y1, y2):
    """Calcula a distancia entre dois pontos num plano dado suas coordenadas
    int, int, int, int -> float"""
    return math.sqrt ((x2 - x1 )**2 + (y2 - y1)**2 )

# letra b
def hipotenusa (cateto_oposto ,cateto_adjacente):
    """Calcula o perimetro de um triangulo a partir de seus catetos
    int, int -> float"""
    return math.sqrt ( cateto_oposto**2 + cateto_adjacente**2)

def perimetro_triangulo(cateto_oposto ,cateto_adjacente):
    """calcula o perimetro do triangulo levando em conta seus catetos e sua hipotenusa , essa que foi definida anteriormente no codigo"""
    return(hipotenusa(cateto_oposto ,cateto_adjacente) + cateto_oposto + cateto_adjacente)

# letra c
def soma_sin_cos (angulo):
    """calcula a soma do quadrado do seno com o quadrado do cosseno usando o modulo math
    int -> float"""
    return math.sin(angulo) ** 2 + math.cos(angulo) ** 2

# questão 5
def area_setor_circular(raio ,angulo = 360):
    """calcula a area de um setor circular para determinado raio e angulo, considerando 360 como valor padrão para o angulo
    int, int -> float"""
    return(math.pi* raio**2 *angulo / 360)

