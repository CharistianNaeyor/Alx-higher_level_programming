#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))




## Advanced tasks
7. Singly linked list


Write a class Node that defines a node of a singly linked list by:
- Private instance attribute: data:
  - property def data(self): to retrieve it
  - property setter def data(self, value): to set it:
     - data must be an integer, otherwise raise a TypeError exception with the message data must be an integer
-Private instance attribute: next_node:
	 - property def next_node(self): to retrieve it
	 - property setter def next_node(self, value): to set it:
	   - next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object
- Instantiation with data and next_node: def __init__(self, data, next_node=None):


And a class SinglyLinkedList that defines a singly linked list by:
- Private instance attribute: head (no setter or getter)
- Simple instantiation: def __init__(self):
- Should be printable:
  - print the entire list in stdout
  - one node number by line
- Public instance method: def sorted_insert(self, value): that inserts a new Node into the correct sorted position in the list (increasing order)
- You are not allowed to import any module
8. Print Square instance  
Write a class Square that defines a square by: (based on 6-square.py)
9. Compare 2 squares  
Write a class Square that defines a square by: (based on 4-square.py)
10. ByteCode -> Python #5  
Write the Python class MagicClass that does exactly the same as the following Python bytecode:
