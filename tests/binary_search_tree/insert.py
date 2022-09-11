from . import Sut


def test_insert_creates_root():
    # arrange
    sut = Sut()

    # act
    result_value = sut.insert(4)
    result = sut.traverse()

    # assert
    assert result_value == True
    assert result == [4]


def test_insert():
    # arrange
    sut = Sut()

    # act

    # https://joshsj.github.io/2022/08/03/(re)learning-cs/trees/#Binary-Search-Tree
    for i in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        sut.insert(i)

    result = sut.traverse("in_order")

    # assert
    assert result == [1, 3, 4, 6, 7, 8, 10, 13, 14]

def test_insert_returns_false_when_duplicate():
    # arrange
    sut = Sut()

    sut.insert(3)

    # act
    result = sut.insert(3)

    # assert
    assert result  == False