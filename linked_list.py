from node import Node

class LinkedList:
    __size = 0
    __head = None

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

    def clear(self, value):
        self.__head = None
        self.__size = 0

    def insert_at(self, index, value):
        if index >= self.__size and index != 0:
            raise IndexError
        if self.__head is None:
            self.__head = Node(value)
        else:
            current_node = self.__head
            i = 0
            while i < index - 1:
                current_node = current_node.next
                i += 1
            current_node.next = Node(value, current_node.next)
        self.__size += 1

    def delete_by_value(self, value):
        if self.__head is None:
            return
        else:
            if self.__head.value == value:
                self.__head = self.__head.next
            else:
                current_node = self.__head.next
                previous_node = self.__head
                while current_node:
                    if current_node.value == value:
                        previous_node.next = current_node.next
                        break
                    else:
                        previous_node = current_node
                        current_node = current_node.next
        self.__size -= 1

    def delete_at(self, index):
        if self.__head is None:
            return
        if index >= self.__size and index != 0:
            raise IndexError
        i = 0
        current_node = self.__head
        while i < index - 1:
            current_node = current_node.next
            i += 1
        current_node.next = current_node.next.next
        self.__size -= 1

    def index_of(self, value):
        if self.__head is None:
            return -1
        else:
            current_node = self.__head
            i = 0
            while i < self.__size:
                if current_node.value == value:
                    return i
                else:
                    current_node = current_node.next
                    i += 1
        return -1

    def contains(self, value):
        if self.index_of(value) > -1:
            return True
        return False

    def length(self):
        return self.__size

    def reverse(self):
        if self.__head is None or self.__size <= 1:
            return
        start = 0
        end = self.__size - 1
        start_node = self.__head

        while start < end:
            i = 0
            current_node = self.__head
            while i < self.__size:
                if i == start:
                    start_node = current_node
                elif i == end:
                    break
                current_node = current_node.next
                i += 1
            temp = start_node.value
            start_node.value = current_node.value
            current_node.value = temp
            start += 1
            end -= 1

    def reverse_list(self):
        current = self.__head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.__head = prev

    def print(self):
        current_node = self.__head
        elements = []
        while current_node:
            elements.append(str(current_node.value))
            current_node = current_node.next
        return ' -> '.join(elements) + ' -> None'
























