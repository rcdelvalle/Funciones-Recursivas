"""
Ejercicio 2.
Genere un diccionario vacío que luego se irá llenando según lo que ingrese el
usuario. Pedir los siguientes datos:
ISBN
Nombre del libro
Stock
Precio del libro
Cuando el usuario ingrese un 0 como ISBN se deberá imprimir:
Todos los datos ingresados
La cantidad total de libros
El monto total de todos los libros
El valor promedio de los libros
"""

# Genera un diccionario vacío
diccionario = {}
isbn = int(input("Ingrese ISBN del libro: "))

while (isbn != 0):
    nombre = input("Ingrese nombre del libro: ")
    stock = input("Stock: ")
    precio = input("Ingrese precio del libro: ")

    # llenando el diccionario según lo que ingrese el usuario.
    diccionario["ISBN"] = isbn
    diccionario["nombre del libro"] = nombre
    diccionario["stock"] = stock
    diccionario["precio"] = precio

    # vuelvo a solicitar el isbn
    isbn = int(input("Ingrese ISBN del libro: "))

can = 0
cantot = 0
# bucle a imprimir
for i in diccionario.values():
    if(can % 4 == 0):
        print(f"ISBN: {i}")
    elif(can % 4 == 1):
        print(f"Nombre del libro: {i}")
    elif(can % 4 == 2):
        print(f"Stock: {i}")
        stock = i
    else:
        print(f"Precio del libro: {i}")
        cantot = cantot + stock
        print(f"La cantidad total de libros: {cantot}")
