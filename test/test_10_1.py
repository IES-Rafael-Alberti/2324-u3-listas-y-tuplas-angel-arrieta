import pytest
from src.Ej_10_1 import min_max


@pytest.mark.parametrize(
    "inLista, outDupla",
    [
        ([76, 34, 29, 50, 41, 11], [11, 76]),
        ([84, 93, 7, 27, 45], [7, 93])
    ]
)
def test_min_max(inLista, outDupla):
    assert min_max(inLista) == outDupla
