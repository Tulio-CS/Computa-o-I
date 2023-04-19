from math import floor


def bolos(a,b,c):
    return floor(min(a / 2 ,  b / 3 , c /5 ))

"""def ingredientes (a,b,c):
    return min(a/2,b/3,c/5)"""

print (bolos(2,50,3))