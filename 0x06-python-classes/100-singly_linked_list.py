#!/usr/bin/python3
"""defining new class"""
class Node:
  """defines a node of a singly linked list """
  def __init__(self, data, next_node=None):
    """creating node.
    Args:
    data: The data of node.
    next_node: The new Node.
    """
    self.data = data
    self.next_node = next_node
  @property
  def data(self):
      return (self._data)
  @data.setter
  def data(self, value):
    if not isinstance(value, int):
        raise TypeError("data must be an integer")
    self._data = value

  @property
  def next_node(self):
      return (self._next_node)
  @next_node.setter
  def next_node(self, value):
    if not isinstance(value, Node) and value is not None:
        raise TypeError("next_node must be a Node object")
    self._next_node = value

class SinglyLinkedList:
  """defines a singly linked list"""
  def __init__(self):
    """creating new linked list"""
    self.head = None
  def sorted_insert(self, value):
    """Inserting new linked list.
    Args:
    Value: new nodes value.
    """
    new_node = Node(value)

    if self.head is None or self.head.data >= value:
     new_node.next_node = self.head
    self.head = new_node
    current = self.head
    while current.next_node is not None and current.next_node.data < value:
        current = current.next_node
    new_node.next_node = current.next_node
    current.next_node = new_node
  def __str__(self):
    nodes = []
    current = self.head
    while current:
        nodes.append(str(current.data))
    current = current.next_node
