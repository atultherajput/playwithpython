#!/usr/bin/env python3
class _Node:
	"""Node class to create new nodes"""
	def __init__(self, data=None, next=None):
		"""Construction of node"""
		self._data = data
		self._next = next

class LinkedList:
	"""Singly Linked List implementation for storage"""
	def __init__(self):
		"""Construction of Linked List"""
		self._head = None
		self._size = 0

	def __str__(self):
		"""Return Linked List Elements"""
		self._current = self._head
		self._output = ""
		while self._current:
			self._output += str(self._current._data) + "-> "
			self._current = self._current._next
		if self._head == None:
			return "Empty Linked List"
		return self._output

	def __len__(self):
		"""Return length of linked list."""
		self._count = 0
		self._current = self._head
		while self._current:
			self._count += 1
			self._current = self._current._next
		return self._count

	def size(self):
		"""Return size of linked list"""
		return self._size

	def is_empty(self):
		"""Return True if Linked List is empty"""
		return self._size == 0

	def value_at(self, index):
		"""Return Value at given index"""
		self._current = self._head
		self._index = index
		count = ans = 0
		while count<= self._index:
			if self._current == None:
				return "List is empty."
			ans = self._current._data
			self._current = self._current._next
			count += 1
		return ans

	def push_front(self, data):
		"""Add element to first position"""
		self._head = _Node(data, self._head)
		self._size += 1

	def pop_front(self):
		"""Delete first element"""
		if self.is_empty():
			return "Linked List is empty"
		self.poped_item = self._head._data
		self._head = self._head._next
		self._size -= 1
		return self.poped_item

	def push_back(self, data):
		"""Add element at last"""
		self._previous = None
		self._current = self._head
		while self._current:
			self._previous = self._current
			self._current = self._current._next
		if self.is_empty():
			return self.push_front(data) #Check This
		self._previous._next = _Node(data)
		self._size +=1

	def pop_back(self):
		"""Delete last Element"""
		self._current = self._head
		if self._current == None:
			return "Empty List"
		while(self._current._next is not None):
			self._current = self._current._next
			if self._current._next._next==None:
				break
		if self._current == self._head:
			ans = self._current._data
			self._head = None
		elif self._current._next == None:
			ans = self._head._next._data
			self._head._next = None
		else:
			ans = self._current._next._data
			self._current._next = None
		self._size -=1
		return ans

	def front(self):
		"""Return First Item"""
		if self.is_empty():
			return "Empty Linked List"
		else:
			return self._head._data



#Test for Linked List:
l = LinkedList()
print(l)
print(l.size())
print(l.is_empty())
l.push_front(4); 	print(l)
print(l.value_at(0))
print(l.is_empty())
l.push_back(5); 	print(l)
print(l.is_empty())
print(l.size())
l.push_front(3); 	print(l)
print(l.value_at(2))
print(l.pop_back())
print(l)
print(l.pop_front())
print(l)
print(l.pop_back())
print(l)
print(len(l))
print(l.is_empty())
print(l.front())
print(l.value_at(2))
print(l)
print(l.pop_back())
