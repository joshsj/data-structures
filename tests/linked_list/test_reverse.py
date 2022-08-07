from src.linked_list import LinkedList
from . import Sut


def test_reverse_correct_for_even_length():
    # arrange
    sut: Sut = LinkedList([1, 2, 3, 4])

    # acts
    sut.reverse()
    result = [n for n in sut]

    # assert
    assert result == [4, 3, 2, 1]


def test_reverse_correct_for_odd_length():
    # arrange
    sut: Sut = LinkedList()
    sut.append(1)
    sut.append(2)
    sut.append(3)

    # act
    sut.reverse()
    result = [n for n in sut]

    # assert
    assert result == [3, 2, 1]
