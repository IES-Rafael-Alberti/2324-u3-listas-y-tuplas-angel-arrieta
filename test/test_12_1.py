import pytest
from src.Ej_12_1 import producto_matrices


@pytest.mark.parametrize(
    "inMatriz_uno, inMatriz_dos, outProducto",
    [
        ((1, 2, 3, 4, 5, 6), (-1, 0, 0, 1, 1, 1,), [-21, 0, 0, 21, 21, 21]),
        ((0, 2, 1, 2, 0, 0), (-1, 0, 1, 2, 0, 1,), [-5, 0, 5, 10, 0, 5])
    ]
)
def test_producto_matrices(inMatriz_uno, inMatriz_dos, outProducto):
    assert producto_matrices(inMatriz_uno, inMatriz_dos) == outProducto
