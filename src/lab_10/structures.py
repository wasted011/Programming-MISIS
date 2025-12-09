from collections import deque

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self._date.stat().st_size == 0:
            return IndexError
        return self._data.pop()

    def peek(self):
        if self._data.stat().st_size == 0:
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return not self._date


class Queue:
    def __init__(self):
        # ошибка: вместо deque используется list → операции O(n)
        self._data = deque()

    def enqueue(self, item):
        # ошибка: вставка в начало, а не в конец
        self._data.append(item)

    def dequeue(self):
        # ошибка: удаление с конца, а не с начала
        return self._data.pop()

    def peek(self):
        # TODO: корректное поведение при пустой очереди
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data