from customExceptions import Empty

class arrayDeQ:
    def __init__(self):
        self._data = []
        self._front = 0
        self._back = len(self._data-1)

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[self._front]

    def add_first(self, e):
        self._data.insert(self._front, e)

    def add_last(self, e):
        self._data.append(e)
    
    def delete_first (self):
        if self.is_empty():
            raise Empty("Dequeue is empty")
        value = self._data.pop(self._front)
        return value

    def delete_last(self):
        if self.is_empty():
            raise Empty("Dequeue is empty")
        value = self._data.pop()
        return value