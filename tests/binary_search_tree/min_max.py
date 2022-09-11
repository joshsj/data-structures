from . import Sut


def test_min_is_correct():
    # act
    sut = Sut()

    for i in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        sut.insert(i)

    # act
    result = sut.min()

    # assert
    assert result == 1


def test_min_returns_no_value_when_empty():
    # act
    result = Sut().min()

    # assert
    assert result is None


def test_max_is_correct():
    # act
    sut = Sut()

    for i in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        sut.insert(i)

    # act
    result = sut.max()

    # assert
    assert result == 14


def test_max_returns_no_value_when_empty():
    # act
    result = Sut().max()

    # assert
    assert result is None
