"""
Ejercicio 4.
Escribir una función recursiva que permita mostrar 
los valores de un vector de
atrás hacia adelante.
"""

vector = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
n = len(vector) - 1

def vector_de_atras_hacia_adelante(n):
    if(n == 0):
        print(vector[0])
    else:
        print(vector[n])
        n = n-1
    
        vector_de_atras_hacia_adelante(n)

vector_de_atras_hacia_adelante(n)
