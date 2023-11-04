import pytest
from src.Ej_2_1 import curso, control_modulo


@pytest.mark.parametrize(
    "inMaterias, outMensaje",
    [
        (["Lenguaje"], "Yo estudio Lenguaje"),
        (["Lenguaje", "Matemáticas", "Tecnología"], "Yo estudio Lenguaje\nYo estudio Matemáticas\nYo estudio Tecnología")
    ]
)
def test_curso(inMaterias, outMensaje):
    assert curso(inMaterias) == outMensaje


@pytest.mark.parametrize(
    "inModulo, outNum_error",
    [
        ("Lenguaje", 0),
        ("__//()", 1),
        ("00__//65", 2),
        ("Te.cnolg/a", 3)
    ]
)
def test_control_modulo(inModulo, outNum_error):
    assert control_modulo(inModulo) == outNum_error
