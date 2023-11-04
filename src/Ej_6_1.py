"""
Ejercicio 3.1.6¶

Escribir un programa que almacene las asignaturas de un curso (por
ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura y elimine
de la lista las asignaturas aprobadas. Al final el programa debe
mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""


def calificar(asignaturas: list, calificaciones: list) -> str:
    repetir = ""
    for materia in asignaturas:
        if calificaciones[asignaturas.index(materia)] < 5:
            repetir += f"{materia}, "
    return repetir[:-2]


def control_modulo(asignatura: str) -> int:
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
    if re.search("[A-Za-z]", asignatura) is None:
        # Modulo sin letras
        if re.search("\d", asignatura) is None:
            # Modulo sin digitos
            fallo = 1
        else:
            # Modulo con digitos
            fallo = 2
        return fallo
    for caracter in asignatura:
        if re.search("\w", caracter) is None:
            fallo = 3
            return fallo
    return fallo


def control_notas(nota: int) -> int:
    """
        Función que revisa la adecuación del input de la nota
        --------------
        nota: int
            nota correspondiente a una asignatura
        return: int
            devuelve 5 si se sale del rango lógico de una nota de asignatura española
            devuelve 0 si no hay fallos.
    """
    fallo = 0
    if not 0 <= nota <= 10:
        fallo = 5
    return fallo


if __name__ == "__main__":
    materias = []
    notas = []
    error = 0
    modulo = ""
    nota = ""
    try:
        #  Proceso
        while modulo != "terminar":
            #  Entrada
            modulo = str(input("Introduce una materia\n('terminar', acaba el programa)\n> "))
            if modulo == "terminar":
                if len(materias) < 1:
                    error = 4
                    raise ValueError(error)
                a_recuperar = calificar(materias, notas)
            elif modulo == "":
                print("Escriba algo, porfavor")
            else:
                error = control_modulo(modulo)
                if error != 0:
                    raise ValueError(error)
                materias.append(modulo)
                while type(nota) is not int:
                    try:
                        #  Entrada
                        nota = int(input("Introduce la nota que tienes en la materia (0-10) > "))
                    except ValueError:
                        print("Introduzca un número entero")
                error = control_notas(nota)
                if error != 0:
                    raise ValueError(error)
                notas.append(nota)
                nota = ""
    #  Salida
        if a_recuperar == "":
            print("No tienes nada que recuperar")
        else:
            print(f"Tienes que recuperar: {a_recuperar}")

    except ValueError:
        if error == 1:
            print(f"{modulo} no es legible")
        elif error == 2:
            print(f"{modulo} no es lógico")
        elif error == 3:
            print(f"{modulo} tiene caracteres extraños en el nombre")
        elif error == 4:
            print("No se han añadido asignaturas")
        elif error == 5:
            print(f"{nota} se sale del rango permitido")
