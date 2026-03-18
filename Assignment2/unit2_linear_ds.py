# unit2_linear_ds.py
# Implementations of DynamicArray, LinkedList, Stack, Queue, and Parentheses Checker

class DynamicArray:
    def __init__(self):
        self._capacity = 2
        self._size = 0
        self._data = [None] * self._capacity

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, x):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = x
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("Pop from empty array")
        val = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return val

    def get(self, i):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of range")
        return self._data[i]

    def set(self, i, x):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of range")
        self._data[i] = x

    def insert(self, i, x):
        if i < 0 or i > self._size:
            raise IndexError("Index out of range")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        for j in range(self._size, i, -1):
            self._data[j] = self._data[j - 1]
        self._data[i] = x
        self._size += 1

    def delete(self, i):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of range")
        for j in range(i, self._size - 1):
            self._data[j] = self._data[j + 1]
        self._data[self._size - 1] = None
        self._size -= 1

    def __str__(self):
        return str([self._data[i] for i in range(self._size)])


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_by_value(self, x):
        temp = self.head
        prev = None
        while temp:
            if temp.data == x:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return True
            prev = temp
            temp = temp.next
        return False

    def search(self, x):
        temp = self.head
        while temp:
            if temp.data == x:
                return True
            temp = temp.next
        return False

    def traverse(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_after_node(self, key, x):
        temp = self.head
        while temp:
            if temp.data == key:
                new_node = Node(x)
                new_node.next = temp.next
                new_node.prev = temp
                if temp.next:
                    temp.next.prev = new_node
                temp.next = new_node
                return True
            temp = temp.next
        return False

    def delete_at_position(self, pos):
        temp = self.head
        index = 0
        while temp:
            if index == pos:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return True
            temp = temp.next
            index += 1
        return False


class Stack:
    def __init__(self):
        self.list = SinglyLinkedList()

    def push(self, x):
        self.list.insert_at_beginning(x)

    def pop(self):
        if not self.list.head:
            raise IndexError("Pop from empty stack")
        val = self.list.head.data
        self.list.head = self.list.head.next
        return val

    def peek(self):
        if not self.list.head:
            raise IndexError("Peek from empty stack")
        return self.list.head.data

    def is_empty(self):
        return self.list.head is None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.head:
            raise IndexError("Dequeue from empty queue")
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        if not self.head:
            raise IndexError("Front from empty queue")
        return self.head.data

    def is_empty(self):
        return self.head is None


def is_balanced(s):
    stack = Stack()
    mapping = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.is_empty() or stack.pop() != mapping[ch]:
                return False
    return stack.is_empty()