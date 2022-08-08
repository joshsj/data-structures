import pytest
from src.trees import BinaryNode as Node


Sut = Node[int]


@pytest.fixture
def sut() -> Sut:
    n = Node(0,
             left=Node(1,
                       left=Node(3,
                                 left=Node(7)
                                 ),
                       right=Node(4)
                       ),

             right=Node(2,
                        left=Node(5,
                                  right=Node(8)
                                  ),
                        right=Node(6,
                                   right=Node(9)

                                   )
                        )
             )
    return n


def invert_is_correct(sut: Sut):
    # act
    sut.invert()
    result = sut.traverse("pre_order")

    # assert
    assert result == [0, 2, 6, 9, 5, 8, 1, 4, 3, 7]
