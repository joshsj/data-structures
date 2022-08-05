from src.linked_list import LinkedList


def test_len_is_zero_when_empty():
    # arrange
    sut = LinkedList()

    # act
    result = len(sut)

    # assert
    assert result == 0


def test_len_is_correct_when_not_empty():
    # arrange
    sut = LinkedList()
    sut.append(1)
    sut.append(2)

    # act
    result = len(sut)

    # assert
    assert result == 2


def test_size_is_zero_when_empty():
    # arrange
    sut = LinkedList()

    # act
    result = sut.size()

    # assert
    assert result == 0


def test_size_is_correct_when_not_empty():
    # arrange
    sut = LinkedList()
    sut.append(1)
    sut.append(2)

    # act
    result = sut.size()

    # assert
    assert result == 2
