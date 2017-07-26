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
			return self.push_front(data)
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

	def back(self):
		"""Return Last Element"""
		self._current = self._head
		while self._current:
			ans = self._current._data
			self._current = self._current._next
		return ans

	def insert(self, index, data):
		"""Insert element at a particular index"""
		self._current = self._head
		self._index = index
		self._element = data
		count = 0
		temp = None
		if self._index == 0:
			return self.push_front(self._element)
		elif self._index < 0:
			return "Negative index are not allowed"
		while count< self._index:
			if self._current == None:
				return "Not Possible"
			temp = self._current
			self._current = self._current._next
			count += 1
		temp._next=_Node(self._element,temp._next)
		self._size += 1

	def erase(self, index):
		"""Delete element at given index"""
		self._current = self._head
		self._index = index
		count = 0
		temp = None
		if self._index == 0:
			return self.pop_front()
		elif self._index < 0:
			return "Negative index are not allowed"
		while count< self._index:
			if self._current == None:
				return "Not Possible"
			temp = self._current
			self._current = self._current._next
			count += 1
		try:
			temp._next= self._current._next
			self._current =None
			self._size -= 1
		except AttributeError:
			print("Index is greater than length of list")

	def value_n_from_end(self, n):
		"""Get value of nth element starting from end"""
		self.n=n
		self.n = int(self.__len__() - self.n -1)
		return self.value_at(self.n)

	def remove_value(self, value):
		"""Delete the first value that it finds."""
		self._value = value
		self._current = self._head
		count = 0
		while self._current is not None:
			if self._current._data==self._value:
				self.erase(count)
				break
			self._current = self._current._next
			count += 1

	def reverse(self):
		"""Reverse Linked List"""
		self._previous = None
		self._current = self._head
		while(self._current is not None):
			next = self._current._next
			self._current._next = self._previous
			self._previous = self._current
			self._current = next
		self._head = self._previous



#Test for Linked List:
if __name__ == '__main__':

	l = LinkedList()
	print(l)
	print(l.size())
	print(l.is_empty())
	l.push_front(4); 	print(l)
	print(l.value_at(0))
	print(l.is_empty())
	l.push_back(6); 	print(l)
	print(l.back())
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
	l.insert(0,5); 		print(l)
	print(l)
	l.erase(2)
	print(l)
	print(l.value_n_from_end(2))
	l.remove_value(4)
	print(l)
	l.push_back(8)
	print(l)
	l.push_back(9)
	print(l)
	l.reverse()
	print(l)
