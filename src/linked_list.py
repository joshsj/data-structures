from __future__ import annotations
from typing import Callable, Generic, Iterable, List, NoReturn, TypeVar, overload

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

    def take_until(self, predicate: Callable[[Node[T]], bool]) -> List[Node[T]]:
        nodes: List[Node[T]] = []

        def move(node: Node[T]) -> List[Node[T]]:
            if predicate(node) or node.next is None:
                return nodes

            nodes.append(node)

            return move(node.next)

        return move(self)

    def walk_by(self, n: int) -> Node[T] | None:
        if not n:
            return self

        node, n_diff = (self.next, -1) if n > 0 else (self.prev, 1)

        if not node:
            return None

        return node.walk_by(n + n_diff)


class IterationNode(Generic[T]):
    def __init__(self, node: Node[T] | None) -> None:
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

    def __init__(self, items: List[T] = []) -> None:
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size: int = 0

        self.extend(items)

    # dunders

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"

    def __iter__(self) -> IterationNode[T]:
        return IterationNode(self.__head)

    def __len__(self) -> int:
        return self.__size

    # indexing

    @overload
    def __getitem__(self, i: int) -> T: ...
    @overload
    def __getitem__(self, i: slice) -> LinkedList[T]: ...

    def __getitem__(self, i: int | slice) -> T | LinkedList[T]:
        return self.__getitem__int(i).value if isinstance(i, int) else self.__getitem__slice(i)

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

    # adding

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
            assert self.__tail is not None

            self.__tail.next = new
            new.prev = self.__tail

            self.__tail = new

        # middle
        else:
            current = self.__getitem__int(i)

            # insert before current
            new.next = current
            new.prev = current.prev

            assert current.prev is not None
            current.prev.next = new
            current.prev = new

        self.__size += 1

    # removing

    def pop(self, i: int | None = None) -> T:
        node = self.__getitem__int(-1 if i is None else i)
        return self.__remove(node).value

    def remove(self, value: T) -> None:
        if not self.__head:
            raise ValueError(value)

        node = self.__head.walk_until(lambda node: node.value == value)

        if not node:
            raise ValueError(value)

        self.__remove(node)

    def __remove(self, node: Node[T]) -> Node[T]:
        if node.prev:
            node.prev.next = node.next
        else:
            # node is head
            self.__head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            # node is tail
            self.__tail = node.prev

        self.__size -= 1

        return node

    def clear(self) -> None:
        self.__head = self.__tail = None
        self.__size = 0

    # utils

    def extend(self, items: Iterable[T]) -> None:
        for item in items:
            self.append(item)

    def count(self, value: T) -> int:
        count = 0

        for n in self:
            count += int(value == n)

        return count

    def copy(self) -> LinkedList[T]:
        return self[:]

    def reverse(self) -> None:
        # reversing does nothing
        if self.__size in [0, 1]:
            return

        assert self.__head is not None
        assert self.__tail is not None

        toSwap = self.__head, self.__tail

        for _ in range(self.__size//2):
            toSwap[0].value, toSwap[1].value = toSwap[1].value, toSwap[0].value

            assert toSwap[0].next is not None
            assert toSwap[1].prev is not None

            toSwap = toSwap[0].next, toSwap[1].prev
