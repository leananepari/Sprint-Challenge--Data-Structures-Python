from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.array = ArrayRingBuffer(self.capacity)

    def append(self, item):
        if self.storage.length == self.capacity:
          self.storage.remove_from_head()
          self.storage.add_to_tail(item)
          self.array.append(item)
        else:
          self.storage.add_to_tail(item)
          self.array.append(item)

    def get(self):
        # # Note:  This is the only [] allowed
        # list_buffer_contents = []

        # # TODO: Your code here
        return self.array.get()

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = []
        self.index = 0

    def append(self, item):
        if self.size == self.capacity:
          self.storage[self.index] = item
          if self.index == self.capacity - 1:
            self.index = 0
          else:
            self.index += 1
        else:
          print('ELSE')
          self.storage.append(item)
          self.size += 1

    def get(self):
        return self.storage

buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')
print(buffer.get())