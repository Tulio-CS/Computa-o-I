#PosNegZero

def PosNegZero(x):
    """Esta função verifica se o argumento fornecido é positivo, negativo ou zero 
    int -> str"""
    if x==0:
        return  str(x) + " e zero"
    else:
        if x<0:
            return str(x) +  " e negativo"
        else:
            return str(x) + " e positivo"



#Classificação

def classificacao(cv, ce, cs, fv, fe, fs):
    """Esta função leva em conta as diversas variaveis para decidir qual dos dois times vai vencer
    int, int, int, int, int, int -> str"""
    if (cv * 3) + ce  > (fv * 3) + fe:
        return "Cormengo"
    else:
        if (cv * 3) + ce  < (fv * 3) + fe:
            return "Flaminthians"
        else:
            if (cv * 3) + ce == (fv * 3) + fe:
                if cs > fs:
                    return "Cormengo"
                else:
                    if cs < fs:
                        return "Flaminthians"
                    elif cs == fs:
                        return "Empate"

#Avioes

def avioes(c, p_compr, p_compet):
    """esta função avalia se a quantidade de papel comprado e suficiente para um determinado de competidores com determinado numero de tentativas
    int, int, int -> str"""
    if c * p_compet <= p_compr:
        return "Suficiente"
    else:
        return "Insuficiente"