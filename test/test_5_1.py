import pytest
from src.Ej_5_1 import ordena_invertido


@pytest.mark.parametrize(
    "inNumeros, outListado",
    [
        ([7, 3, 8, 1], "8, 7, 3, 1"),
        ([5, 3, 1, 2, 8, 4, 10], "10, 8, 5, 4, 3, 2, 1"),

    ]
)
def test_ordena_invertido(inNumeros, outListado):
    assert ordena_invertido(inNumeros) == outListado
