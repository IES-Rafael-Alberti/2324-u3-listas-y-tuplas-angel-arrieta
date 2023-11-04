"""
Ejercicio 3.1.12¶

Escribir un programa que almacene las matrices A=(1 2 3 4 5 6) y B=(−1 0 0 1 1 1)
en una lista y muestre por pantalla su producto. Nota: Para representar
matrices mediante listas usar listas anidadas, representando cada vector
fila en una lista.
"""


def producto_matrices(primera_matriz: tuple, segunda_matriz: tuple) -> list:
    producto = []
    for numero in segunda_matriz:
        adjunto = 0
        for valor in primera_matriz:
            adjunto += numero * valor
        producto.append(adjunto)
    return producto


if __name__ == "__main__":
    #  Entrada
    matriz_A = (1, 2, 3, 4, 5, 6)
    matriz_B = (-1, 0, 0, 1, 1, 1)
    #  Proceso
    producto = producto_matrices(matriz_A, matriz_B)
    #  Salida
    print(producto)
