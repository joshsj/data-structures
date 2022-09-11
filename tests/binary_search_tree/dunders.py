from . import Sut


def test_len_is_zero_when_empty():
    # arrange
    sut = Sut()

    sut.insert(1)
    sut.insert(2)

    # act
    result = len(sut)

    # assert
    assert result == 2


def test_len_is_correct_when_not_empty():
    # act
    result = len(Sut())

    # assert
    assert result == 0
