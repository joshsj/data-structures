from src.linked_list import LinkedList
from . import Sut


def test_get_with_index_returns_correct_value_when_positive():
    # arrange
    sut: Sut = LinkedList()
    sut.append(1)
    sut.append(2)
    sut.append(3)

    # act
    result = sut[1]

    # assert
    assert result == 2


def test_get_with_index_returns_correct_value_when_negative():
    # arrange
    sut: Sut = LinkedList()
    sut.append(1)
    sut.append(2)
    sut.append(3)

    # act
    result = sut[-2]

    # assert
    assert result == 2


def test_set_with_index_stores_value():
    # arrange
    i = 1
    value = 10

    sut: Sut = LinkedList()
    sut.append(1)
    sut.append(2)

    # act
    sut[i] = value
    result = sut[i]

    # assert
    assert result == value
