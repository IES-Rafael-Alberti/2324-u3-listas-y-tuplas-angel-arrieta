import pytest
from src.Ej_6_1 import calificar, control_modulo, control_notas


@pytest.mark.parametrize(
    "inMaterias, inNotas, outMensaje",
    [
        (["Ingles"], [9], ""),
        (["Lengua"], [4], "Lengua"),
        (["Lengua", "Mates_2", "Tecno"], [4, 8, 2], "Lengua, Tecno"),
    ]
)
def test_calificar(inMaterias, inNotas, outMensaje):
    assert calificar(inMaterias, inNotas) == outMensaje


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
