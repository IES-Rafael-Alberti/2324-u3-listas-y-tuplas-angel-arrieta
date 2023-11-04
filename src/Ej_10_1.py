"""
Ejercicio 3.1.10¶

Escribir un programa que almacene en una lista los siguientes precios:
50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor
de los precios.
"""


def min_max(lista: list) -> list:
    min_max = []
    min_max.append(min(lista))
    min_max.append(max(lista))
    return min_max


if __name__ == "__main__":
    #  Entrada
    lista = [50, 75, 46, 22, 80, 65, 8]
    #  Proceso
    min_max = min_max(lista)
    #  Salida
    print(f"El menor precio es {min_max[0]} y el mayor {min_max[1]}")
