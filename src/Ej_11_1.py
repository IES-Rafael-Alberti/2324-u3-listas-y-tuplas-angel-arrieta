"""
Ejercicio 3.1.11¶

Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2)
en dos listas y muestre por pantalla su producto escalar.
"""


def producto_escalar(vectorA: tuple, vectorB: tuple) -> int:
    producto = 0
    for numero in vectorA:
        producto += (numero * vectorB[vectorA.index(numero)])
    return producto


if __name__ == "__main__":
    #  Entrada
    primera_flecha = (1, 2, 3)
    segunda_flecha = (-1, 0, 2)
    #  Proceso
    direccion_escalada = producto_escalar(primera_flecha, segunda_flecha)
    #  Salida
    print(direccion_escalada)
