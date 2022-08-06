from cgitb import reset
from src.linked_list import LinkedList


def test_swap_correct_for_even_length():
    # arrange
    sut = LinkedList()
    sut.append(1)
    sut.append(2)
    sut.append(3)
    sut.append(4)

    # act
    sut.reverse()
    result = [n for n in sut]

    # assert
    assert result == [4, 3, 2, 1]
