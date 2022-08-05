from __future__ import annotations
from operator import ilshift
from typing import Callable, Dict, Generic, MutableSequence,   NoReturn, Type, TypeVar
T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, next_: Node[T] | None = None) -> None:
        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        return f"{type(self).__name__}(value={self.value}, next={self.next})"

    def walk(self, i: int) -> Node[T] | None:
        if not i:
            return self

        if not self.next:
            return None

        return self.next.walk(i - 1)


class IterationNode(Generic[T]):
    def __init__(self, node: Node[T]) -> None:
        self.node = node

    def __next__(self) -> T | NoReturn:
        if self.node is None:
            raise StopIteration

        current_value = self.node.value

        self.node = self.node.next

        return current_value


# TODO inherit from MutableSequence[T]
class LinkedList(Generic[T]):
    """
    Linked List implementation of native list data type

    See: https://docs.python.org/3/tutorial/datastructures.html
    """

    def __init__(self) -> None:
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size: int = 0

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"

    def __iter__(self) -> IterationNode[T]:
        return IterationNode(self.__head)

    def __len__(self) -> int:
        return self.__size

    def __getitem__(self, i: int | slice) -> T | LinkedList[T] | NoReturn:
        if isinstance(i, int):
            return self.__getitem__int(i)

        if isinstance(i, slice):
            return self.__getitem__slice(i)

        raise TypeError(i)

    def __getitem__int(self, i: int) -> int | NoReturn:
        # check valid index
        if i < 0 or i >= self.__size:
            raise IndexError(i)

        # check we have some node
        if self.__head is None:
            return None

        node = self.__head.walk(i)

        if not node:
            raise IndexError(i)

        return node.value

    def __getitem__slice(self, i: slice) -> LinkedList[T]:
        raise NotImplementedError

    def size(self) -> int:
        return self.__size

    def append(self, value: T):
        self.__size += 1
        new = Node(value)

        if self.__head is None:
            self.__tail = self.__head = new
            return

        # update the chain & tail pointer
        self.__tail.next = new
        self.__tail = new

    def clear(self) -> None:
        self.__head = self.__tail = None
        self.__size = 0
