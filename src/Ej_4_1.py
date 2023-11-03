"""
Ejercicio 3.1.4¶

Escribir un programa que pregunte al usuario los números ganadores
de la lotería primitiva, los almacene en una lista y los muestre
por pantalla ordenados de menor a mayor.
"""


def ordena(numero: str) -> str:
    numero = list(numero)
    numero.sort()
    numero = "".join(numero)
    return numero


def control_numloto(numero: str) -> int:
    """
        Función que revisa la adecuación del input de la loteria
        --------------
        numero: int
            loteria que se quiere revisar
        return: int
            depende de que incumpla, devuelve un número
            asociado a un error cada uno más importante que otro:
            1 - Tiene no númericos
            2 - No tiene la cantidad de digitos adecuada
    """
    import re
    fallo = 0
    for digito in numero:
        if re.search("\d", digito) is None:
            fallo = 1
            return fallo
    if len(numero) != 5:
        fallo = 2
        return fallo
    return fallo


if __name__ == "__main__":
    error = 0
    loteria = ""
    try:
        #  Entrada
        loteria = input("Dime los numeros ganadores\n(max longitud 5) > ")
        #  Proceso
        error = control_numloto(loteria)
        if error != 0:
            raise ValueError(error)
        loteria_ordenada = ordena(loteria)
    #  Salida
        print(loteria_ordenada)
    except ValueError:
        if error == 1:
            print(f"{loteria} no es un número")
        elif error == 2:
            print(f"{loteria} no tiene 5 digitos")

