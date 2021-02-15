from sys import stdin
import math
import unittest

def adicion(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def inversavector(a):
    ans = []
    for i in range(len(a)):
        ans =  ans + [-1*(a[i])]
    return ans


def multiplicacionvector(a, b):
    ans = []
    for i in range(len(a)):
        print(a[i])
        ans = ans + [a[i]*b]
    return ans


def adicionmatrices(a, b):
    ans = []
    if len(a) != len(b):
        return "Las matrices no tienen las mismas dimensiones"
    else:
        for i in range(len(a)):
            if len(a[i]) != len(b[i]):
                return "Las matrices no tienen las mismas dimensiones"
            else:
                ans = ans + [adicion(a[i],b[i])]
        return ans

def inversamatriz(a):
    ans = [0]*len(a)
    for i in range(len(a)):
        ans[i] = inversavector(a[i])
    return ans

def multiplicacionmatriz(a, b):
    ans = []
    for i in range(len(a)):
        print(a[i])
        ans = ans +  [multiplicacionvector(a[i], b)]
    return ans

def transpuesta(a):
    ans = []
    for i in range(len(a[0])):
        r = [x[i] for x in a]
        ans.append(r)
    return ans

def conjugadavector(a):
    return [a[0], (a[1])*-1]

def conjugadamatriz(a):
        ans = []
        for i in range(len(a)):
            ans = ans + [conjugadavector(a[i])]
        return ans

def adjuntamatriz(a):
    return conjugadamatriz(transpuesta(a))

def productovector(a, b):
    r = (0+0)
    for i in range(len(a)):
        t = (a[i]*b[i])
        r = r + t
    return r

def productomatriz(a, b):
    if len(a) != len(b[0]):
        return "Las matrices no tienen las dimensiones adecuadas"
    else:
        matriz = [[None] * len(b[0])for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                l = [f[j] for f in b]
                matriz[i][j] = productovector(a[i], l)
        return matriz

def productointerno(a, b):
    r = complex(0,0)
    for i in range(len(a)):
        return (adicion(r, productovector(conjugadavector(b[i]),a[i])))








def main():
    a = [1,2]
    b = [2,3]
    print(productointerno(a, b))
main()