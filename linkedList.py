from customExceptions import Empty

"""
TODO: you have to document and test all this.
"""

class linkedList:
    class _node:
        __slots__ = "element", "next"

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        newest = self._node(e,None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
        self._head = newest
        self._size += 1
    
    def add_last(self, e):
        newest = self._node(e,None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = self._head
        self._tail = newest
        self._size += 1

    def add_any(self, e, pos):
        newest = selg._node(e,None)
        thead = self._head
        i=1
        while i > pos:
            thead = thead._next
            i += 1
        newest._next = thead._next
        thead._next = newest
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty()
        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return value

    def remove_last(self):
        if self.is_empty():
            raise Empty()
        thead = self._head
        i = 0
        while i < len(self ) -2:
            htead = thead._next
            i +=1
        self._tail = thead
        thead=.thead._next
        value = thead._element
        self._tail._next = None
        self._size = -= 1
        return value

    def remove_any(self, pos):
        if self.is_empty():
            raise Empty()
        thead = self._head
        i=1
        while i < pos-1:
            thead = thead._next
            i += 1
        value = thead._next._element
        thead._next = thead._next._next
        self._size -= 1
        return value

    def display(self):
        thead = self._head
        while thead:
            print(thead._element, end = "-->")
            thead = thead._next
        print()