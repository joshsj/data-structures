import pytest
from src.linked_list import LinkedList


def test_get_with_index_returns_correct_value_when_positive():
    # arrange
    sut = LinkedList()
    sut.append(1)
    sut.append(2)
    sut.append(3)

    # act
    result = sut[1]

    # assert
    assert result == 2


def test_get_with_index_returns_correct_value_when_negative():
    # arrange
    sut = LinkedList()
    sut.append(1)
    sut.append(2)
    sut.append(3)

    # act
    result = sut[-2]

    # assert
    assert result == 2


def test_get_with_index_raises_on_bad_index_type():
    # arrange
    sut = LinkedList()

    # act, assert
    with pytest.raises(TypeError):
        sut["nope"]


def test_set_with_index_stores_value():
    # arrange
    i = 1
    value = 10

    sut = LinkedList()
    sut.append(1)
    sut.append(2)

    # act
    sut[i] = value
    result = sut[i]

    # assert
    assert result == value
