"""
Ejercicio 3.1.1¶

Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla.
"""


def curso(materias: list,) -> str:
    respuesta = ""
    for modulo in materias:
        respuesta += f"{modulo} "
    return respuesta[:-1]


def control_modulo(modulo: str) -> int:
    """
        Función que revisa la adecuación del input del modulo
        --------------
        modulo: str
            asignatura a añadir al curso
        return: int
            depende de que incumpla, devuelve un número
            asociado a un error cada uno más importante que otro:

            1 - el modulo no tiene ningun caracter legible
            2 - el modulo no contiene ninguna letra
            3 - el modulo contiene algun caracter no palabra
            devuelve 0 si no hay fallos.
        """
    import re
    fallo = 0
    if re.search("[A-Za-z]", modulo) is None:
        # Modulo sin letras
        if re.search("\d", modulo) is None:
            # Modulo sin digitos
            fallo = 1  # El modulo no tiene ningun caracter legible
        else:
            # Modulo con digitos
            fallo = 2  # El modulo tiene como mínimo digitos
        return fallo
    for caracter in modulo:
        if re.search("\w", caracter) is None:
            fallo = 3  # No es un caracter palabra
            return fallo
    return fallo


if __name__ == "__main__":
    materias = []
    modulo = ""
    error = 0
    #  Proceso
    try:
        while modulo != "terminar":
            #  Entrada
            modulo = str(input("Introduce una materia\n('terminar', acaba el programa)\n> "))
            if modulo == "terminar":
                if len(materias) < 1:
                    error = 4
                    raise ValueError(error)
                asignaturas = curso(materias)
            elif modulo == "":
                print("Escriba algo, porfavor")
            else:
                error = control_modulo(modulo)
                if error != 0:
                    raise ValueError(error)
                materias.append(modulo)
    #  Salida
        print(asignaturas)
    except ValueError:
        if error == 1:
            print(f"{modulo} no es legible")
        elif error == 2:
            print(f"{modulo} no es lógico")
        elif error == 3:
            print(f"{modulo} tiene caracteres extraños en el nombre")
        elif error == 4:
            print("No se han añadido asignaturas")
