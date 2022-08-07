from src.linked_list import LinkedList
from . import Sut


def test_evaluates_to_false_when_empty():
    # arrange
    sut: Sut = LinkedList()

    # act
    result = bool(sut)

    # assert
    assert result == False


def test_evaluates_to_true_when_has_items():
    # arrange
    sut: Sut = LinkedList()
    sut.append(1)

    # act
    result = bool(sut)

    # assert
    assert result == True


def test_count_is_correct():
    # arrange
    sut: Sut = LinkedList()
    sut.append(1,)
    sut.append(2)
    sut.append(2)
    sut.append(3)

    # act
    result = sut.count(2)

    # assert
    assert result == 2


def test_len_is_zero_when_empty():
    # arrange
    sut: Sut = LinkedList()

    # act
    result = len(sut)

    # assert
    assert result == 0


def test_len_is_correct_when_not_empty():
    # arrange
    sut: Sut = LinkedList()
    sut.append(1)
    sut.append(2)

    # act
    result = len(sut)

    # assert
    assert result == 2


def test_returns_correct_values():
    # arrange
    sut: Sut = LinkedList()
    sut.append(1)
    sut.append(2)
    sut.append(3)

    # act
    result = [n for n in sut]

    # assert
    assert result == [1, 2, 3]
