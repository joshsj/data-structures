from src.linked_list import LinkedList


def test_returns_correct_values():
    # arrange
    sut = LinkedList()
    sut.append(1)
    sut.append(2)
    sut.append(3)

    # act
    result = [n for n in sut]

    # assert
    assert result == [1, 2, 3]
