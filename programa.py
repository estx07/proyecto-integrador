# Consigna:
# Codificar en Python un programa que contenga las siguientes condiciones:

# El usuario debe ingresar 5 números enteros, los cuales serán almacenados en una lista.
# Función Suma: recibe como parámetro la lista y devuelve la suma total de todos sus elementos.
# Función Promedio: recibe como parámetro la lista y devuelve el promedio de sus elementos.
# Función Máximo: recibe como parámetro la lista y devuelve el valor máximo de todos los elementos que contiene.
# Función Mínimo: recibe como parámetro la lista y devuelve el valor mínimo de todos los elementos que contiene.

# --------------------------------------------------------------------------------------------------------------


def funcion_suma (list_number):
    suma  = 0 
    for numbers in range (5):
        suma += list_number [numbers]
    return suma

def funcion_ingresar_datos():
    list_number = []
    for numbers in range (5):
        numbers_add = int(input("Ingrese un número: "))
        list_number.append(numbers_add)
    return list_number

lista = funcion_ingresar_datos()
suma = funcion_suma(lista)
print(suma) 