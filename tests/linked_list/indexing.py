from . import Sut


def test_get_with_index_returns_correct_value_when_positive():
    # arrange
    sut = Sut()
    sut.append(1)
    sut.append(2)
    sut.append(3)

    # act
    result = sut[1]

    # assert
    assert result == 2


def test_get_with_index_returns_correct_value_when_negative():
    # arrange
    sut = Sut()
    sut.append(1)
    sut.append(2)
    sut.append(3)

    # act
    result = sut[-2]

    # assert
    assert result == 2


def test_set_with_index_stores_value():
    # arrange
    i = 1
    value = 10

    sut = Sut()
    sut.append(1)
    sut.append(2)

    # act
    sut[i] = value
    result = sut[i]

    # assert
    assert result == value


def test_del_removes_value():
    # arrange
    sut = Sut([1, 2, 3])

    # act
    del sut[1]
    result = [n for n in sut]

    # assert
    assert result == [1, 3]
