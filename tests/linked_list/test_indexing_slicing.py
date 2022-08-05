from typing import Type
import pytest
from src.linked_list import LinkedList


def test_returns_current_value_for_int():
    # arrange
    sut = LinkedList()
    sut.append(1)
    sut.append(2)
    sut.append(3)

    # act
    result = sut[1]

    # assert
    assert result == 2


def test_returns_correct_values_for_slice():
    # arrange
    sut = LinkedList()
    sut.append(1)
    sut.append(2)
    sut.append(3)

    # act
    result = sut[1:3]

    # assert
    assert result == [2, 3]


def test_returns_no_values_for_out_of_range_slice():
    # arrange
    sut = LinkedList()
    sut.append(1)

    # act
    result = sut[1:3]

    # assert
    assert result == []


def test_raises_on_invalid_index_value():
    # arrange
    sut = LinkedList()

    # act, assert
    with pytest.raises(IndexError):
        sut[-1]


def test_raises_on_invalid_index_type():
    # arrange
    sut = LinkedList()

    # act, assert
    with pytest.raises(TypeError):
        sut["nope"]
