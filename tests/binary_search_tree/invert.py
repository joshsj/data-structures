from . import Sut
import pytest


@pytest.fixture
def sut() -> Sut:
    sut = Sut()

    # https://joshsj.github.io/2022/08/03/(re)learning-cs/trees/#Binary-Search-Tree
    for i in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        sut.insert(i)

    return sut


def test_invert_is_correct(sut: Sut):
    # act
    sut.invert()
    result = sut.traverse("in_order")

    # assert
    assert result == [14, 13, 10, 8, 7, 6, 4, 3, 1]
