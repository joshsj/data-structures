from src.linked_list import LinkedList
from . import Sut


def evaluates_to_false_when_empty():
    # arrange
    sut: Sut = LinkedList()

    # act
    result = bool(sut)

    # assert
    assert result == False


def evaluates_to_true_when_has_items():
    # arrange
    sut: Sut = LinkedList([1])

    # act
    result = bool(sut)

    # assert
    assert result == True


def count_is_correct():
    # arrange
    sut: Sut = LinkedList([1, 2, 2, 3])

    # act
    result = sut.count(2)

    # assert
    assert result == 2


def len_is_zero_when_empty():
    # arrange
    sut: Sut = LinkedList()

    # act
    result = len(sut)

    # assert
    assert result == 0


def len_is_correct_when_not_empty():
    # arrange
    sut: Sut = LinkedList([1, 2])

    # act
    result = len(sut)

    # assert
    assert result == 2


def returns_correct_values():
    # arrange
    sut: Sut = LinkedList([1, 2, 3])

    # act
    result = [n for n in sut]

    # assert
    assert result == [1, 2, 3]
