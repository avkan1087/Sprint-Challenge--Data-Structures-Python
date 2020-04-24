from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            if self.current != None:
                if self.current.next:
                    self.current.next.delete()
                    self.current.insert_after(item)
                    self.current = self.current.next
                else:
                    self.storage.remove_from_head()
                    self.storage.add_to_head(item)
                    self.current = self.storage.head
            else:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # make sure to filter out None valus
        node = self.storage.head
        while node != None:
            if node.value != None:
                list_buffer_contents.append(node.value)

            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
