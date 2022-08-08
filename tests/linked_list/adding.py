import pytest
from src.linked_list import LinkedList
from . import Sut


@pytest.fixture
def sut() -> Sut:
    return LinkedList([1, 2, 3])


def append_works():
    # arrange
    sut: Sut = LinkedList()
    sut.append(1)
    sut.append(2)
    sut.append(3)

    # act
    result = [n for n in sut]

    # assert
    assert result == [1, 2, 3]


def insert_correct_value_at_start(sut: Sut):
    # arrange
    value = 4

    # act
    sut.insert(0, value)
    result = [n for n in sut]

    # assert
    assert result == [4, 1, 2, 3]


def insert_correct_value_in_middle(sut: Sut):
    # arrange
    value = 4

    # act
    sut.insert(2, value)
    result = [n for n in sut]

    # assert
    assert result == [1, 2, 4, 3]


def insert_correct_value_at_end(sut: Sut):
    # arrange
    value = 4

    # act
    sut.insert(3, value)
    result = [n for n in sut]

    # assert
    assert result == [1, 2, 3, 4]


def extend_correct_values():
    # arrange
    sut: Sut = LinkedList()

    # act
    sut.extend([1, 2])
    result = [n for n in sut]

    # assert
    assert result == [1, 2]
