from __future__ import annotations
from audioop import tostereo
import enum
from importlib.metadata import SelectableGroups
from typing import Callable, Generic, NoReturn, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(
            self,
            value: T, next_: Node[T] | None = None,
            prev: Node[T] | None = None) -> None:

        self.value = value
        self.next = next_
        self.prev = prev

    def __repr__(self) -> str:
        return f"{type(self).__name__}(value={self.value}, next={self.next is not None}, prev={self.prev is not None})"

    def walk_until(self, predicate: Callable[[Node[T]], bool]) -> Node[T] | None:
        if predicate(self):
            return self

        return self.next.walk_until(predicate) if self.next else None

    def walk_by(self, n: int) -> Node[T] | None:
        if not n:
            return self

        node, n_diff = (self.next, -1) if n > 0 else (self.prev, 1)

        if not node:
            return None

        return node.walk_by(n + n_diff)

    def swap(self, other: Node[T]) -> None:
        # store other values
        temp = other.prev, other.next

        # apply self values to other
        other.prev, other.next = self.prev, self.next

        # apply other values to self
        self.prev, self.next = temp


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
            return self.__getitem__int(i).value

        if isinstance(i, slice):
            return self.__getitem__slice(i)

        raise TypeError(i)

    def __getitem__int(self, i: int) -> Node[T] | NoReturn:
        # TODO add handling to start at tail of closer

        # ensure valid index
        if i >= self.__size or i < -self.__size:
            raise IndexError(i)

        # adjust i for negative indexing starting at -1
        start, n = (self.__tail, i+1) if i < 0 else (self.__head, i)

        if not start:
            raise IndexError(i)

        result = start.walk_by(n)

        if not result:
            raise IndexError(i)

        return result

    def __getitem__slice(self, i: slice) -> LinkedList[T]:
        raise NotImplementedError

    def __setitem__(self, i: int, value: T) -> None:
        self.__getitem__int(i).value = value

    def size(self) -> int:
        return self.__size

    def clear(self) -> None:
        self.__head = self.__tail = None
        self.__size = 0

    def count(self, value: T) -> int:
        count = 0
        for n in self:
            if n == value:
                count += 1

        return count

    def reverse(self) -> None:
        if self.__size < 2:
            return

        toSwap = self.__head, self.__tail

        # until middle node
        for _ in range(self.__size//2):
            # store the next nodes
            toSwap = toSwap[0].next, toSwap[1].prev

            # retrieve the current nodes
            Node.swap(toSwap[0].prev, toSwap[1].next)

        # swap pointers
        self.__head, self.__tail = self.__tail, self.__head

    def append(self, value: T) -> None:
        self.insert(self.__size, value)

    def insert(self, i: int, value: T) -> None:
        new = Node(value)

        # TODO fix repeated size increment
        if self.__head is None:
            self.__tail = self.__head = new

        # start
        elif not i:
            self.__head.prev = new
            new.next = self.__head

            self.__head = new

        # end
        elif i == self.__size or i == -1:
            self.__tail.next = new
            new.prev = self.__tail

            self.__tail = new

        # middle
        else:
            current = self.__getitem__int(i)

            new.next = current
            new.prev = current.prev

            current.prev.next = new
            current.prev = new

        self.__size += 1

    def pop(self, i: int | None = None) -> T:
        node = self.__getitem__int(-1 if i is None else i)
        self.__remove(node)
        return node.value

    def remove(self, value: T) -> None:
        if not self.__head:
            raise ValueError(value)

        node = self.__head.walk_until(lambda node: node.value == value)

        if not node:
            raise ValueError(value)

        self.__remove(node)

    def __remove(self, node: Node[T]) -> Node[T]:
        # point head forwards if needed
        if node is self.__head:
            self.__head = self.__head.next
            self.__head.prev = None

        # point tail backwards if needed
        elif node is self.__tail:
            self.__tail = self.__tail.prev
            self.__tail.next = None

        # fuggetaboutit
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self.__size -= 1
