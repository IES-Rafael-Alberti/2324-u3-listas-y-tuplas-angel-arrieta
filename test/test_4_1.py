import pytest
from src.Ej_4_1 import ordena, control_numloto


@pytest.mark.parametrize(
    "inNumero, outOrdenado",
    [
        ("09153", "01359"),
        ("77610", "01677")
    ]
)
def test_ordena(inNumero, outOrdenado):
    assert ordena(inNumero) == outOrdenado


@pytest.mark.parametrize(
    "inNumero, outError",
    [
        ("77610", 0),
        ("8AT56", 1),
        ("45", 2),
        ("937522", 2),
        ("-07655", 1)
    ]
)
def test_control_numloto(inNumero, outError):
    assert control_numloto(inNumero) == outError
