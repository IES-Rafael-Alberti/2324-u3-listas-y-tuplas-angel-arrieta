import pytest
from src.Ej_11_1 import producto_escalar


@pytest.mark.parametrize(
    "inVectorA, inVectorB, outProd_escalar",
    [
        ((1, 2, 3), (-1, 0, 2), 5),
        ((3, 4, 2), (0, -2, 4), 0)
    ]
)
def test_producto_escalar(inVectorA, inVectorB, outProd_escalar):
    assert producto_escalar(inVectorA, inVectorB) == outProd_escalar
