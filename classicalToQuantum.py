import math
import unittest

######################### Operaciones necesarias ##############################
def suma(a, b):
    x = a[0]+b[0]
    y = a[1]+b[1]
    return (x, y)

def multiplicacion(a, b):
    e = []
    im = []
    for i in range(len(a)):
        for j in range(len(b)):
            if i == 0 and j == 0:
                e.append(a[i]* b[j])
            elif i == 0 and j == 1:
                im.append(a[i]*b[j])
            elif i == 1 and j == 0:
                im.append(a[i]*b[j])
            else:
                e.append(-1*a[i]*b[j])

    return ((e[0]+e[1]), (im[0]+ im[1]))

def multiplicaVectores(a, b):
    ans = (0,0)
    for i in range(len(a)):
        ans = suma(ans, multiplicacion(a[i], b[i]))
    return ans

def multiplicaVectoresReales(a, b):
    ans = 0
    for i in range(len(a)):
        ans += a[i]*b[i]
    return ans

def productoMatricesReales(a,b):
    ans = []
    for i in range(len(a)):
        fila = []
        for j in range(len(b[0])):
            temp = 0
            for k in range(len(b)):
                mult = a[i][k] * b[k][j]
                temp += mult
            fila.append(temp)
        ans.append(fila)
    return ans

def productoMatrizVectorReal(a, b):
    if len(b[0])!= len(a):
        return "Las dimensiones son incorrectas"
    else:
        ans = []
        for i in range(len(b)):
            ans.append(multiplicaVectoresReales(a, b[i]))
        return ans


def productoMatricesC(a, b):
    ans = []
    for i in range(len(a)):
        fila = []
        for j in range(len(b[0])):
            temp = (0, 0)
            for k in range(len(b)):
                mult = multiplicacion(a[i][k], b[k][j])
                temp += suma(mult, temp)
            fila.append(temp)
        ans.append(fila)
    return ans

def productoMatrizVectorC(a,b):
    if len(b[0]) != len(a):
        return "Las dimensiones son incorrectas"
    else:
        ans = []
        for i in range(len(b)):
            ans.append(multiplicaVectores(a,b[i]))
        return ans

########################## Simulaciones #############################
def canicas(matriz, vector, clicks):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[j][i]:
                matriz[j][i] = 1
            else:
                matriz[j][i] = 0
    for c in range(int(clicks)):
        ans = [[0 for i in range(len(vector[0]))] for j in range(len(matriz))]
        for i in range(len(matriz)):
            for j in range(len(vector[0])):
                for k in range(len(matriz[0])):
                    ans[i][j] = ans[i][j] + (matriz[i][k]*vector[k][j])
    return ans

def rendijasReales(rendijas, objetivo, inicial, estado):
    if (len(inicial) != objetivo) or (len(inicial[0]) != objetivo):
        return "Las matrices no son proporcionales."
    else:
        for i in range(rendijas):
            inicial = productoMatricesReales(inicial, inicial)
        return productoMatrizVectorReal(estado, inicial)

def rendijasCuanticas(rendijas, objetivo, inicial, estado):
    if len(inicial) != objetivo or (len(inicial[0]) != objetivo):
        return "Las matrices no son proporcionales."
    else:
        for i in range(rendijas):
            inicial = productoMatricesC(inicial, inicial)
        return productoMatrizVectorC(estado, inicial)

