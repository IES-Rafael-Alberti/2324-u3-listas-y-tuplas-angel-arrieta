"""
Ejercicio 3.1.5¶

Escribir un programa que almacene en una lista los números del 1 al 10
y los muestre por pantalla en orden inverso separados por comas.
"""


def ordena_invertido(numeros: list) -> str:
    listado = ""
    numeros.sort()
    numeros.reverse()
    for num in numeros:
        listado += f"{num}, "
    return listado[:-2]


if __name__ == "__main__":
    #  Entrada
    lista = [4, 2, 9, 7, 5, 8, 10, 3, 6, 1]
    #  Proceso
    ordenado = ordena_invertido(lista)
    #  Salida
    print(ordenado)
