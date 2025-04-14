from node import Node

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def append(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            current_node = self.__head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(value)
        self.__size += 1

    def prepend(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            self.__head = Node(value, self.__head)
        self.__size += 1

    def clear(self):
        self.__head = None
        self.__size = 0

    def insert_at(self, index, value):
        if index < 0 or index > self.__size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(value)
            return
        current = self.__head
        for _ in range(index - 1):
            current = current.next
        current.next = Node(value, current.next)
        self.__size += 1

    def delete_by_value(self, value):
        if self.__head is None:
            return
        if self.__head.value == value:
            self.__head = self.__head.next
            self.__size -= 1
            return

        current_node = self.__head.next
        previous_node = self.__head
        while current_node:
            if current_node.value == value:
                previous_node.next = current_node.next
                self.__size -= 1
                return
            previous_node = current_node
            current_node = current_node.next

    def delete_at(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.__head = self.__head.next
        else:
            current = self.__head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.__size -= 1

    def index_of(self, value):
        current = self.__head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def contains(self, value):
        return self.index_of(value) != -1

    def length(self):
        return self.__size

    def reverse(self):
        current = self.__head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.__head = prev

    def has_cycle(self):
        fast = self.__head
        slow = self.__head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


    def print(self):
        current_node = self.__head
        elements = []
        while current_node:
            elements.append(str(current_node.value))
            current_node = current_node.next
        return ' -> '.join(elements) + ' -> None'