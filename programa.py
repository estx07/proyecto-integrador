# Consigna:
# Codificar en Python un programa que contenga las siguientes condiciones:

# El usuario debe ingresar 5 números enteros, los cuales serán almacenados en una lista.
# Función Suma: recibe como parámetro la lista y devuelve la suma total de todos sus elementos.
# Función Promedio: recibe como parámetro la lista y devuelve el promedio de sus elementos.
# Función Máximo: recibe como parámetro la lista y devuelve el valor máximo de todos los elementos que contiene.
# Función Mínimo: recibe como parámetro la lista y devuelve el valor mínimo de todos los elementos que contiene.

# -------------------------------------------------------------------------------------

# Función ingresar datos en una lista Daia D. : 
def funcion_ingresar_datos():
    List_Number = []
    for numbers in range (5):
        numbers_add = int(input("Ingrese un numero: "))
        List_Number.append (numbers_add)
    return List_Number


# Función Promedio Susana G. :
def funcion_promedio(List_number):
    avg = 0
    for numbers in range (5):
        avg += List_number[numbers]
    avg /= 5 
    avg = int(avg)
    return avg


# Función Suma Agustina C. :
def funcion_suma (List_number):
    suma  = 0 
    for numbers in range (5):
        suma += List_number [numbers]
    return suma


#aqui funcion minimo 


#Función maximo Edgar G. :
def funcion_maximo(List_number):
    maximo = List_number[0]
    for x in List_number:
        if x > maximo :
             maximo = x
    return maximo


lista = funcion_ingresar_datos()

promedio = funcion_promedio(lista)
suma = funcion_suma(lista)
maximo = funcion_maximo(lista)
#aqui variable minimo con su llamada

print(promedio)
print(suma) 
print(maximo)
# aqui print de llamada min