from src.linked_list import LinkedList


def test_clear_removes_all_values():
    # arrange
    sut = LinkedList()

    # act
    sut.clear()
    result = [n for n in sut]

    # assert
    assert not result
