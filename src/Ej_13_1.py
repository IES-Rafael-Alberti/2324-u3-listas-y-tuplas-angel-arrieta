"""
Ejercicio 3.1.13¶

Escribir un programa que pregunte por una muestra de números, separados
por comas, los guarde en una lista y muestre por pantalla su media y
desviación típica.
"""


def dividir(lista: str) -> list:
    lista = lista.split(",")
    listado = []
    for numero in lista:
        listado.append(numero.strip())
    return listado


def control_lista(lista: list) -> int:
    import re
    fallo = 0
    for numero in lista:
        if re.search("\D", numero) is not None:
            fallo = 1
    return fallo


def adecuacion_lista(lista: list) -> list:
    listado = []
    for numero in lista:
        listado.append(int(numero))
    return listado


def media_aritmetica(lista: list) -> int:
    suma = 0
    cantidad_datos = len(lista)
    for numero in lista:
        suma += numero
    media = suma/cantidad_datos
    return media


if __name__ == "__main__":
    error = 0
    try:
        listado = str(input("Ingresa una lista de numeros separada por comas\n> "))
        lista_dividida = dividir(listado)
        error = control_lista(lista_dividida)
        if error != 0:
            raise ValueError(error)
        lista_tipada = adecuacion_lista(lista_dividida)
        media = media_aritmetica(lista_tipada)
        print(f"La media aritmetica de tus numeros {lista_tipada} es {media}")
    except ValueError:
        if error == 1:
            print("Algún elemento de la lista contiene caracteres no númericos")
