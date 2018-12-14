class Node:
  """Node Class"""
  def __init__(self, value):
    self.next = None
    self.value = value

class LinkedList:
  """Single Linked List Class"""
  def __init__(self):
    self.root = None
    self.length = 0

  def insert(self, value, index = 0):
    """Will insert value at specified index
       Returns IndexError if index out of range"""
    if index > self.length:
      raise IndexError(f"index {index} out of range")
      
    if not self.root:
      self.root = Node(value)      

    else:
      i = 0
      temp = self.root
      prev = None
      while(temp and i != index):
        prev = temp
        temp = temp.next        
        i += 1

      newNode = Node(value)

      if prev == None:        
        newNode.next = temp
        self.root = newNode

      else:        
        newNode.next = temp
        prev.next = newNode

    self.length += 1

  def remove(self, value):
    """Removes item or returns ValueError if item not in list"""
    prev = None
    temp = self.root

    while(temp and temp.value != value):
      prev = temp
      temp = temp.next

    if temp == None:
      raise ValueError(f"{value} not in list")

    elif prev == None:
      self.root = self.root.next

    else:
      prev.next = temp.next

    self.length -= 1

  def index(self, value):
    """Returns index of value or ValueError if value not in list"""
    i = 0
    temp = self.root
    while(temp and temp.value != value):
      temp = temp.next
      i += 1

    if temp == None:
      raise ValueError(f"{value} not in list")
    return i

  def __len__(self):
    return self.length

  def print_list(self):
    temp = self.root
    while(temp):
      print(temp.value)
      temp = temp.next
