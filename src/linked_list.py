from __future__ import annotations
from typing import Callable, Generic, Iterable, Iterator,  MutableSequence, NoReturn, TypeVar, overload

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(
            self,
            value: T,
            next_: Node[T] | None = None,
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


class IterationNode(Generic[T]):
    def __init__(self, start: Node[T] | None) -> None:
        self.current = start

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T | NoReturn:
        if self.current is None:
            raise StopIteration

        current_value = self.current.value

        self.current = self.current.next

        return current_value


class LinkedList(MutableSequence[T], Generic[T]):
    """
    Linked List implementation of native list data type

    See: https://docs.python.org/3/tutorial/datastructures.html
    """

    def __init__(self, items: Iterable[T] = []) -> None:
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size: int = 0

        self.extend(items)

    # dunders

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"

    def __iter__(self) -> Iterator[T]:
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

    def __delitem__(self, index: int) -> None:
        self.pop(index)

    # adding

    def append(self, value: T) -> None:
        self.insert(self.__size, value)

    def insert(self, index: int, value: T) -> None:
        new = Node(value)

        if self.__head is None:
            self.__tail = self.__head = new

        # start
        elif index == 0:
            self.__head.prev = new
            new.next = self.__head

            self.__head = new

        # end
        elif index == self.__size or index == -1:
            assert self.__tail is not None

            self.__tail.next = new
            new.prev = self.__tail

            self.__tail = new

        # middle
        else:
            current = self.__getitem__int(index)

            # insert before current
            new.next = current
            new.prev = current.prev

            assert current.prev is not None
            current.prev.next = new
            current.prev = new

        self.__size += 1

    # removing

    def pop(self, index: int | None = None) -> T:
        node = self.__getitem__int(index if index is not None else -1)
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

    def extend(self, values: Iterable[T]) -> None:
        for value in values:
            self.append(value)

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
