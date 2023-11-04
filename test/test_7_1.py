import pytest
from src.Ej_7_1 import borra_multitres


@pytest.mark.parametrize(
    "inListado, outSinmultiplos",
    [
        (["q", "w", "e", "r", "t"], ["e", "q", "t", "w"]),
        (["a", "s", "d", "f", "g", "h", "j"], ["a", "d", "g", "h", "s"]),
    ]
)
def test_borra_multitres(inListado, outSinmultiplos):
    assert borra_multitres(inListado) == outSinmultiplos
