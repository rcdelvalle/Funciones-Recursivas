"""
Ejercicio 3.
Implementar una función que calcule la suma de todos los números enteros
comprendidos entre cero y un número entero positivo dado.
"""

num = int(input("Ingrese un numero entero: "))

def suma_num_entero(numero):
    suma = numero * (numero+1) / 2
    return suma

print(f"la suma de los números enteros \
comprendidos entre cero y {num} es {suma_num_entero(num)}")