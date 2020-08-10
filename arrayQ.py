from customExceptions import Empty

class arrayQ:
    def __init__(self):
        self._data = []
        self._size = 0
        self._front = 0
    
    """
    this wont work >>
    def __len(self):
        return len(self._data)
    """

    def is_empty(self):
        return len(self._data) == 0
    
    #from here
    def enqueue(self, e):
        self._data.append(e)
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        #return self._data.pop(self._data[0])
        value = self._data[self._front]
        self._data[self._front] = None
        self._front += 1
        self._size -= 1


    def first(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[self._front]
        