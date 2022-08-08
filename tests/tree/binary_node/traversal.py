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


def pre_order_is_correct_order(sut: Sut):
    # act
    result = sut.traverse("pre_order")

    # assert
    assert result == [0, 1, 3, 7, 4, 2, 5, 8, 6, 9]


def in_order_is_correct_order(sut: Sut):
    # act
    result = sut.traverse("in_order")

    # assert
    assert result == [7, 3, 1, 4, 0, 5, 8, 2, 6, 9]


def post_order_is_correct_order(sut: Sut):
    # act
    result = sut.traverse("post_order")

    # assert
    assert result == [7, 3, 4, 1, 8, 5, 9, 6, 2, 0]
