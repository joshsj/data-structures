from src.linked_list import LinkedList


def test_evaluates_to_false_when_empty():
    # arrange
    sut = LinkedList()

    # act
    result = bool(sut)

    # assert
    assert result == False


def test_evaluates_to_true_when_has_items():
    # arrange
    sut = LinkedList()
    sut.append(1)

    # act
    result = bool(sut)

    # assert
    assert result == True
