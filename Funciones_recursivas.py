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

while (nro_suc != 0):
    nombre = input("Nombre de sucursal: ")
    ventas = int(input("Cantidad de ventas: "))
    total = int(input("Venta total de la sucursal: "))

    # append nro suc, nombre, ventas, total
    # llenando la lista según lo que ingrese el usuario.
    lista.append(nro_suc)
    lista.append(nombre)
    lista.append(ventas)
    lista.append(total)

    # vuelvo a solicitar el nro suc
    nro_suc = int(input("Nro de sucursal: "))

cantidad = 0
# bucle a imprimir
for i in lista:
    if(cantidad % 4 == 0):
        print(f"Nro Sucursal: {i}")
    elif (cantidad % 4 == 1):
        print(f"Sucursal: {i}")
    elif (cantidad % 4 == 2):    
        print(f"Ventas: {i}")
        ventas = i
    else:
        print(f"Total sucursal: {i}")
        total = i
        
        # Se deberá sacar el promedio de ventas en pesos de esa sucursal
        promedio = total / ventas
        print(f"Promedio: {promedio}")

    cantidad += 1
    
    

