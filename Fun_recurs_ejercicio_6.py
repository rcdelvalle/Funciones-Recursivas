"""
Ejercicio 6.
Dado un nro iniciar una cuenta regresiva por medio de una función recursiva,
imprimir la cuenta y al llegar a cero imprimir por pantalla "¡Booom!".
"""
import time

nro = int(input("ingrese un numero: "))

def cuenta_regresiva(nro):

    if(nro == 0):
        print("¡Booom!")
    
    else: # imprimir la cuenta
        print(nro)
        nro = nro - 1
        time.sleep(1)
        
        cuenta_regresiva(nro)

cuenta_regresiva(nro)