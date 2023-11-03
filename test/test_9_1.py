import pytest
from src.Ej_9_1 import cuenta_vocales, control_palabra


@pytest.mark.parametrize(
    "inPalabra, outLetras",
    [
        ("Murcielago", [["a", 1], ["e", 1], ["i", 1], ["o", 1], ["u", 1]]),
        ("Ensaimada", [["a", 3], ["e", 1], ["i", 1]]),
        ("Xlyptyck", [])
    ]
)
def test_cuenta_vocales(inPalabra, outLetras):
    assert cuenta_vocales(inPalabra) == outLetras


@pytest.mark.parametrize(
    "inPalabra, outNum_error",
    [
        ("Me gusta la pizza", 2),
        ("Colchones", 0),
        ("M3 gust4 1a pi7z4", 2),
        ("R3g4r1amos", 1),
    ]
)
def test_control_palabra(inPalabra, outNum_error):
    assert control_palabra(inPalabra) == outNum_error
