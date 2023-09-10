"""
Ejercicio 5.
Implementar una función recursiva que permita recorrer una matriz y 
mostrar sus
valores.
"""

m = [[8, 14, -6], [12,7,4], [-11,3,21]]
n = 0
i = 0

def recorrer_matriz(n,i):
    
    if(n == len(m)-1):
        if(i == len(m[n])-1):
            print(m[n][i])
        else:
            print(m[n][i])
            i = i + 1
            recorrer_matriz(n,i)
    else:
        if(i == len(m[n])-1):
            print(m[n][i])
            i = 0
            n = n + 1

        print(m[n][i])
        i = i + 1
        recorrer_matriz(n,i)

recorrer_matriz(n,i)