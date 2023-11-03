"""
Ejercicio 3.1.9¶

Escribir un programa que pida al usuario una palabra y muestre por pantalla
el número de veces que contiene cada vocal.
"""


def cuenta_vocales(palabra: str) -> list:
    palabra = palabra.lower()
    vocales = [["a", 0], ["e", 0], ["i", 0], ["o", 0], ["u", 0]]
    for caracter in palabra:
        if caracter == "a":
            vocales[0][1] += 1
        if caracter == "e":
            vocales[1][1] += 1
        if caracter == "i":
            vocales[2][1] += 1
        if caracter == "o":
            vocales[3][1] += 1
        if caracter == "u":
            vocales[4][1] += 1
    resultado = []
    resultado.extend(vocales)
    for cuenta in vocales:
        if cuenta[1] == 0:
            resultado.remove(cuenta)
    return resultado


def control_palabra(palabra: str) -> int:
    """
        Función que revisa la adecuación del input de la palabra
        --------------
        palabra: str
            palabra a comprobar
        return: int
            depende de que incumpla, devuelve un número
            asociado a un error cada uno más importante que otro:

            1 - Tiene caracteres no letras
            2 - Es una frase
            devuelve 0 si no hay fallos.
    """
    import re
    fallo = 0
    if re.search(" ", palabra) is not None:
        fallo = 2
    else:
        for caracter in palabra:
            if re.search("[A-Za-z]", caracter) is None:
                fallo = 1
    return fallo


if __name__ == "__main__":
    error = 0
    try:
        palabra = str(input("Dime una palabra para contarle las vocales\n> "))
        error = control_palabra(palabra)
        if error != 0:
            raise ValueError(error)
        vocales_contadas = cuenta_vocales(palabra)
        if vocales_contadas == []:
            print("No se han contado vocales")
        else:
            salida = "Se han contado: "
            for dupla in vocales_contadas:
                salida += f"{dupla[1]} {dupla[0]}, "
            print(salida[:-2])
    except ValueError:
        if error == 1:
            print(f"{palabra} contiene caracteres que no son letra")
        elif error == 2:
            print(f"{palabra} es una frase (contiene espacios)")
