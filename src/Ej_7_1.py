"""
Ejercicio 3.1.7¶

Escribir un programa que almacene el abecedario en una lista,
elimine de la lista las letras que ocupen posiciones múltiplos de 3,
y muestre por pantalla la lista resultante.
"""


def borra_multitres(abece: list) -> list:
    """
    Quita las letras que en orden son múltiplos de 3
    ---------------
    abece:  list
        lista con el abecedario
    return:  list
        abecedario sin las letras correspondientes
    """
    listado = []
    abece.sort()
    for letra in abece:
        if (abece.index(letra)+1) % 3 == 0:
            continue
        else:
            listado.append(letra)
    return listado


if __name__ == "__main__":
    #  Entrada
    abecedario = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ñ",
                  "z", "x", "c", "v", "b", "n", "m"]
    #  Proceso
    sin_multitres = borra_multitres(abecedario)
    #  Salida
    print(sin_multitres)
