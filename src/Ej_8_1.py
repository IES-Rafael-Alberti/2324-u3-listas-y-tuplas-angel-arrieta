"""
Ejercicio 3.1.8¶

Escribir un programa que pida al usuario una palabra y muestre por
pantalla si es un palíndromo.
"""


def palindromia(palabra: str) -> bool:
    """
        Función que comprueba si la palabra es palindroma
        ----------------
        palabra: string
            palabra a comprobar
        return: boolean
            devuelve True o False dependiendo de si se cumple la condición
    """
    listada = []
    palabra = palabra.lower()
    for caracter in palabra:
        listada.append(caracter)
    listada.reverse()
    reversa = "".join(listada)
    if reversa == palabra:
        return True
    else:
        return False


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
        #  Entrada
        palabra = str(input("Dime una palabra\ny te dire si es palindroma\n> "))
        #  Proceso
        error = control_palabra(palabra)
        if error != 0:
            raise ValueError(error)
        es_palindromo = palindromia(palabra)
    #  Salida
        if es_palindromo is True:
            print(f"{palabra} es un palindromo")
        else:
            print(f"{palabra} no es palindromo")
    except ValueError:
        if error == 1:
            print(f"{palabra} contiene caracteres que no son letra")
        elif error == 2:
            print(f"{palabra} es una frase (contiene espacios)")
