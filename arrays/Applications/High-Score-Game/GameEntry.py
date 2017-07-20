#!/usr/bin/env python3
class GameEntry:
	"""Represents one entry of a list of high scores."""
	def __init__(self, name, score):
		self._name = name
		self._score = score

	def get_name(self):
		return self._name

	def get_score(self):
		return self._score

	def __str__(self):
		return '({0}, {1})'.format(self._name, self._score) 		#e.g., '(Bob, 90)'

#Test for GameEntry
'''g = GameEntry('Atul', 99)
print(type(g))
print(g.get_name(), g.get_score())
print(g)'''
