from src.binary_search_tree import Node
import pytest
from . import Sut


@pytest.fixture
def sut() -> Sut:
    sut = Sut()

    # https://joshsj.github.io/2022/08/03/(re)learning-cs/trees/#Binary-Search-Tree
    for i in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        sut.insert(i)

    return sut


def test_root_gets_correct_node():
    # arrange
    parent_1 = Node(1)
    parent_2 = Node(2, parent=parent_1)
    sut = Node(3, parent=parent_2)

    # act
    result = sut.root

    # assert
    assert result is parent_1
