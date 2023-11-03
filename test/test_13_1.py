import pytest
from src.Ej_13_1 import dividir, control_lista, adecuacion_lista, media_aritmetica, desviacion


@pytest.mark.parametrize(
    "inListado, outLista",
    [
        ("1, 2, 6, 4, 3, 8, 5", ["1", "2", "6", "4", "3", "8", "5"]),
        ("5, 7, 5,6,4, 3,9, 15,22", ["5", "7", "5", "6", "4", "3", "9", "15", "22"])
    ]
)
def test_dividir(inListado, outLista):
    assert dividir(inListado) == outLista


@pytest.mark.parametrize(
    "inListado, outError",
    [
        (["1", "6", "45", "23", "15", "84"], 0),
        (["/4", "a", "te5", "78"], 1)
    ]
)
def test_control_lista(inListado, outError):
    assert control_lista(inListado) == outError


@pytest.mark.parametrize(
    "inLista, outListado",
    [
        (["1", "6", "45", "23", "15", "84"], [1, 6, 45, 23, 15, 84]),
        (["14", "4", "35", "78"], [14, 4, 35, 78])
    ]
)
def test_adecuacion_lista(inLista, outListado):
    assert adecuacion_lista(inLista) == outListado


@pytest.mark.parametrize(
    "inLista, outMedia",
    [
        ([1, 6, 45, 23, 15, 84], 29),
        ([14, 4, 3, 78], 24.75)
    ]
)
def test_media_aritmetica(inLista, outMedia):
    assert media_aritmetica(inLista) == outMedia


@pytest.mark.parametrize(
    "inLista, inMedia, outDesviacion",
    [
        ([26, 10], 18, 8),
        ([12, 10, 13, 17], 13, 2.55)
    ]
)
def test_desviacion(inLista, inMedia, outDesviacion):
    assert desviacion(inLista, inMedia) == outDesviacion
