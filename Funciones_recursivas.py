"""
Ejercicio 1.
Genere una lista vacía que luego se irá llenando según lo que ingrese el
usuario.

Pedir los siguientes datos:
Nro de sucursal
Nombre de sucursal
Cantidad de ventas
Venta total de la sucursal

Se deberá sacar el promedio de ventas en pesos de esa sucursal
Cuando el usuario ingrese un 0 como nro de sucursal se deberá imprimir:
Todos los datos ingresados
El promedio de cada sucursal
El total vendido por toda la cadena

"""
# Genera una lista vacía
lista = []
nro_suc = int(input("Nro de sucursal: "))
# El total vendido por toda la cadena
total_cadena = 0

while (nro_suc != 0):
    nombre = input("Nombre de sucursal: ")
    ventas = int(input("Cantidad de ventas: "))
    total = int(input("Venta total de la sucursal: "))
    total_cadena += total

    # append nro suc, nombre, ventas, total
    # llenando la lista según lo que ingrese el usuario.
    lista.append([nro_suc, nombre, ventas, total])
    

    # vuelvo a solicitar el nro suc
    nro_suc = int(input("Nro de sucursal: "))


# bucle a imprimir
for suc in lista:
    
    print(f"nro Sucursal: {suc[0]}")
    print(f"Sucursal: {suc[1]}")
    print(f"Ventas: {suc[2]}")
    print(f"Total sucursal: {suc[3]}")
        
    # Se deberá sacar el promedio de ventas en pesos de esa sucursal
    promedio = suc[3] / suc[2]
    print(f"Promedio: {promedio}")

print(f"Total cadena:{total_cadena}")

    
    
    

