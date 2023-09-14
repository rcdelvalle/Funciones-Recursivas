# Puede utilizar la siguiente librería para generar los nros random 
# al principio
# del archivo
from random import *

"""
Ejercicio 7.
Escriba una función recursiva para contar en cuantos intentos se puede 
adivinar
el número de un dado.
Pasos a seguir:
Genere un nro random
Solicite al usuario que ingrese un nro
Verifique si es correcto informe que acerto en X intento
Si no acertó, cuente el intento y vuelva a solicitar el nro
"""

"""
Escriba una función recursiva para contar en cuantos intentos se puede 
adivinar
el número de un dado.
"""
def adivinar(x, n):
    # Solicite al usuario que ingrese un nro
    nro_usuario = int(input("Ingrese un nro: "))
    n += 1

    # Verifique si es correcto informe que acerto en X intento
    if(nro_usuario == x):
        print(f"Acertaste en {n} intentos")
    else:
        # Si no acertó, cuente el intento y vuelva a solicitar el nro
        adivinar(x,n)


# Genere un nro random
nro = randint(1,6)

adivinar(nro,0)
