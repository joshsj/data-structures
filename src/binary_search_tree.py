from __future__ import annotations
from typing import Generic, List, Literal, TypeVar


T = TypeVar("T")


def pre_order(node: Node[T] | None) -> List[T]:
    return ([node.value] + pre_order(node.left) + pre_order(node.right)) if node else []


def in_order(node: Node[T] | None) -> List[T]:
    return (in_order(node.left) + [node.value] + in_order(node.right)) if node else []


def post_order(node: Node[T] | None) -> List[T]:
    return (post_order(node.left) + post_order(node.right) + [node.value]) if node else []


TraversalMode = Literal["pre_order", "in_order", "post_order"]
Traversers = {
    "pre_order": pre_order,
    "in_order": in_order,
    "post_order": post_order
}


class Node(Generic[T]):
    def __init__(
            self,
            value: T,
            parent: Node[T] | None = None,
            left: Node[T] | None = None,
            right: Node[T] | None = None) -> None:
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    @property
    def root(self) -> Node[T]:
        return self if self.parent is None else self.parent.root

    def invert(self) -> None:
        if self.left:
            self.left.invert()

        if self.right:
            self.right.invert()

        self.left, self.right = self.right, self.left

    def insert(self, value: T) -> bool:
        # TODO fix comparability
        if value < self.value:
            if not self.left:
                self.left = Node(value, self)
                return True

            return self.left.insert(value)

        if value > self.value:
            if not self.right:
                self.right = Node(value, self)
                return True

            return self.right.insert(value)

        # value == self.value
        return False

    def min(self) -> T:
        return self.left.min() if self.left else self.value

    def max(self) -> T:
        return self.right.max() if self.right else self.value


class BinarySearchTree(Generic[T]):

    def __init__(self):
        self.__root: Node[T] | None = None
        self.__size = 0

    def traverse(self, mode: TraversalMode = "pre_order") -> List[T]:
        return Traversers[mode](self.__root)

    def invert(self) -> None:
        if self.__root:
            self.__root.invert()

    def insert(self, value: T) -> bool:
        if not self.__root:
            self.__root = Node(value, None)
            self.__size = 1
            return True

        result = self.__root.insert(value)
        self.__size += int(result)
        return result

    def __len__(self):
        return self.__size

    def min(self) -> T | None:
        return self.__root.min() if self.__root else None

    def max(self) -> T | None:
        return self.__root.max() if self.__root else None
