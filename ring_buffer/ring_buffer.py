from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
          if self.storage.tail == self.current:
            self.current = self.storage.head
            self.storage.head.value = item
          else:
            self.current = self.current.next
            self.current.value = item
        else:
          self.storage.add_to_tail(item)
          self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while True:
          list_buffer_contents.append(node.value)
          if node.next is None:
            break
          else:
            node = node.next
  
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = [None] * capacity
        self.index = 0

    def append(self, item):
        if self.size == self.capacity:
          self.storage[self.index] = item
          if self.index == self.capacity - 1:
            self.index = 0
          else:
            self.index += 1
        else:
          for i in range(len(self.storage)):
            if self.storage[i] is None:
              print('here', i)
              self.storage[i] = item
              print('here', i, self.storage)
              self.size += 1
              break

    def get(self):
      arr = []
      for i in self.storage:
        if i is None:
          break
        else:
          arr.append(i)
      return arr

buffer = ArrayRingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')
print(buffer.get())