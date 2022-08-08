from __future__ import annotations
from typing import Generic, List, Literal, TypeVar

T = TypeVar("T")


def pre_order(node: BinaryNode[T] | None) -> List[T]:
    return ([node.value] + pre_order(node.left) + pre_order(node.right)) if node else []


def in_order(node: BinaryNode[T] | None) -> List[T]:
    return (in_order(node.left) + [node.value] + in_order(node.right)) if node else []


def post_order(node: BinaryNode[T] | None) -> List[T]:
    return (post_order(node.left) + post_order(node.right) + [node.value]) if node else []


TraversalMode = Literal["pre_order", "in_order", "post_order"]
Traversers = {
    "pre_order": pre_order,
    "in_order": in_order,
    "post_order": post_order
}


class BinaryNode(Generic[T]):
    def __init__(
            self, value: T,
            parent: BinaryNode[T] | None = None,
            left: BinaryNode[T] | None = None,
            right: BinaryNode[T] | None = None) -> None:
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    @property
    def root(self) -> BinaryNode[T]:
        return self if self.parent is None else self.parent.root

    def traverse(self, mode: TraversalMode = "pre_order") -> List[T]:
        return Traversers[mode](self)

    def invert(self) -> None:
        if self.left:
            self.left.invert()

        if self.right:
            self.right.invert()

        self.left, self.right = self.right, self.left
