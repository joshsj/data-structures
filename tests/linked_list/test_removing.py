import pytest
from src.linked_list import LinkedList


@pytest.fixture
def sut():
    sut = LinkedList()
    sut.append(1)
    sut.append(2)
    sut.append(3)
    return sut


def test_remove_correct_value_in_middle(sut: LinkedList):
    # act
    sut.remove(2)
    result = [n for n in sut]

    # assert
    assert result == [1, 3]


def test_remove_correct_value_at_start(sut: LinkedList):
    # act
    sut.remove(1)
    result = [n for n in sut]

    # assert
    assert result == [2, 3]


def test_remove_correct_value_at_end(sut: LinkedList):
    # act
    sut.remove(3)
    result = [n for n in sut]

    # assert
    assert result == [1, 2]


def test_remove_raises_when_value_missing(sut: LinkedList):
    with pytest.raises(ValueError):
        sut.remove(-1)


def test_pop_removes_end_value_with_no_index(sut: LinkedList):
    # act
    result_value = sut.pop()
    result = [n for n in sut]

    # assert
    assert result_value == 3
    assert result == [1, 2]


def test_pop_removes_correct_value_with_index(sut: LinkedList):
   # act
    result_value = sut.pop(1)
    result = [n for n in sut]

    # assert
    assert result_value == 2
    assert result == [1, 3]


def test_clear_removes_all_values(sut: LinkedList):
    # act
    sut.clear()
    result = [n for n in sut]

    # assert
    assert not result
    assert not sut.size()
