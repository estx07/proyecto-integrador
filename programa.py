# Consigna:
# Codificar en Python un programa que contenga las siguientes condiciones:

# El usuario debe ingresar 5 números enteros, los cuales serán almacenados en una lista.
# Función Suma: recibe como parámetro la lista y devuelve la suma total de todos sus elementos.
# Función Promedio: recibe como parámetro la lista y devuelve el promedio de sus elementos.
# Función Máximo: recibe como parámetro la lista y devuelve el valor máximo de todos los elementos que contiene.
# Función Mínimo: recibe como parámetro la lista y devuelve el valor mínimo de todos los elementos que contiene.

# --------------------------------------------------------------------------------------------------------------

#Lista
def funcion_ingresar_datos():
    List_Number = []
    for numbers in range (5):
     numbers_add = int(input("Ingrese un numero: "))
     List_Number.append (numbers_add)
    return List_Number