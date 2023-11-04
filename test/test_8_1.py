import pytest
from src.Ej_8_1 import palindromia, control_palabra


@pytest.mark.parametrize(
    "inPalabra, outBooleano",
    [
        ("Aranara", True),
        ("Saracatunga", False)
    ]
)
def test_palindromia(inPalabra, outBooleano):
    assert palindromia(inPalabra) == outBooleano


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
