from src.trees import BinaryNode


def root_gets_correct_node():
    # arrange
    parent_1 = BinaryNode(1)
    parent_2 = BinaryNode(2, parent=parent_1)
    sut = BinaryNode(3, parent=parent_2)

    # act
    result = sut.root

    # assert
    assert result is parent_1

