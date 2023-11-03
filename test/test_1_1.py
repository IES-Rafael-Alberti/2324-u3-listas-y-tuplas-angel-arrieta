import pytest
from src.Ej_1_1 import curso, control_modulo


@pytest.mark.parametrize(
    "inMaterias, outMensaje",
    [
        (["Lenguaje"], "Lenguaje"),
        (["Lenguaje", "Matemáticas", "Tecnología"], "Lenguaje Matemáticas Tecnología")
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
