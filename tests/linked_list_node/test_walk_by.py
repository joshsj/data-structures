from typing import Tuple

import pytest
from src.linked_list import Node

Nodes = Tuple[Node[int], Node[int], Node[int]]


@pytest.fixture
def nodes() -> Nodes:
    left = Node(0)
    middle = Node(1)
    right = Node(2)

    left.next = middle
    middle.next = right

    right.prev = middle
    middle.prev = left

    return (left, middle, right)


def test_returns_current_node_when_zero(nodes: Nodes):
    # arrange
    left, *_ = nodes

    # act
    result = left.walk_by(0)

    # assert
    assert result is left


def test_returns_forward_node_when_positive(nodes: Nodes):
    # arrange
    left, *_, right = nodes

    # act
    result = left.walk_by(2)

    # assert
    assert result is right


def test_returns_backward_node_when_negative(nodes: Nodes):
    # arrange
    *_, middle, right = nodes

    # act
    result = right.walk_by(-1)

    # assert
    assert result is middle


def test_returns_nothing_when_n_too_large(nodes: Nodes):
    # arrange
    left, *_ = nodes

    # act
    result = left.walk_by(5)

    # assert
    assert result is None
