class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self, _size: int = 0):
        self.head = None
        self._size = _size

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self._size += 1
            return "Первый элемент добавлен"

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self_size += 1

    def prepend(self, value):
        """Добавить элемент в начало списка"""
        new_node = Node(value, next=self.head)
        self.head = new_node
        self_size += 1

    def insert(self, idx, value):
        """Вставка по индексу — неполная реализация, есть ошибки"""
        if idx < 0:
            raise IndexError("Negative index is not supported")

        if idx == 0:
            self.prepend(value)
            return

        current = self.head
        if idx <= self._size:
            for _ in range(idx - 1):
                current = current.next
        else:
            return "Выход за границы"

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"