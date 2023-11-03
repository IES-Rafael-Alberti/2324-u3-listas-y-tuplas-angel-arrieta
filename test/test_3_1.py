import pytest
from src.Ej_3_1 import calificaciones, control_modulo, control_notas


@pytest.mark.parametrize(
    "inMaterias, inNotas, outMensaje",
    [
        (["Lengua"], [5], "En Lengua has sacado 5"),
        (["Lengua", "Mates_2", "Tecno"], [5, 7, 9], "En Lengua has sacado 5\nEn Mates_2 has sacado 7\nEn Tecno has sacado 9"),
    ]
)
def test_calificaciones(inMaterias, inNotas, outMensaje):
    assert calificaciones(inMaterias, inNotas) == outMensaje


@pytest.mark.parametrize(
    "inModulo, outFallo",
    [
        ("Lenguaje", 0),
        ("__//()", 1),
        ("00__//65", 2),
        ("Te.cnolg/a", 3)
    ]
)
def test_control_modulo(inModulo, outFallo):
    assert control_modulo(inModulo) == outFallo


@pytest.mark.parametrize(
    "inNota, outFallo",
    [
        (7, 0),
        (-1, 5),
        (13, 5)
    ]
)
def test_control_notas(inNota, outFallo):
    assert control_notas(inNota) == outFallo
