from . import Sut
from src.binary_search_tree import Node as Node
import pytest


@pytest.fixture
def sut() -> Sut:
    sut = Sut()

    # https://joshsj.github.io/2022/08/03/(re)learning-cs/trees/#Binary-Search-Tree
    for i in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        sut.insert(i)

    return sut


def test_pre_order_is_correct_order(sut: Sut):
    # act
    result = sut.traverse("pre_order")

    # assert
    assert result == [8, 3, 1, 6, 4, 7, 10, 14, 13]


def test_in_order_is_correct_order(sut: Sut):
    # act
    result = sut.traverse("in_order")

    # assert
    assert result == [1, 3, 4, 6, 7, 8, 10, 13, 14]


def test_post_order_is_correct_order(sut: Sut):
    # act
    result = sut.traverse("post_order")

    # assert
    assert result == [1, 4, 7, 6, 3, 13, 14, 10, 8]
