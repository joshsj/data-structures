import pytest
from src.linked_list import LinkedList
from . import Sut


@pytest.fixture
def sut() -> Sut:
    return LinkedList([1, 2, 3])


def test_remove_correct_value_in_middle(sut: Sut):
    # act
    sut.remove(2)
    result = [n for n in sut]

    # assert
    assert result == [1, 3]


def test_remove_correct_value_at_start(sut: Sut):
    # act
    sut.remove(1)
    result = [n for n in sut]

    # assert
    assert result == [2, 3]


def test_remove_correct_value_at_end(sut: Sut):
    # act
    sut.remove(3)
    result = [n for n in sut]

    # assert
    assert result == [1, 2]


def test_remove_raises_when_value_missing(sut: Sut):
    with pytest.raises(ValueError):
        sut.remove(-1)


def test_pop_removes_end_value_with_no_index(sut: Sut):
    # act
    result_value = sut.pop()
    result = [n for n in sut]

    # assert
    assert result_value == 3
    assert result == [1, 2]


def test_pop_removes_correct_value_with_index(sut: Sut):
   # act
    result_value = sut.pop(1)
    result = [n for n in sut]

    # assert
    assert result_value == 2
    assert result == [1, 3]


def test_clear_removes_all_values(sut: Sut):
    # act
    sut.clear()
    result = [n for n in sut]

    # assert
    assert not result
    assert not len(result)
