#!/usr/bin/env python3.5


def pick_word():

	word = input("Type a word: ")
	word = word.split(' ')
	
	if len(word) == 1:

		word = ''.join(word)
		single_translate(word)

	else:

		multiple_translate(word)

def single_translate(word):

	vowels = ['a', 'e', 'i', 'o', 'u']

	if word[0] in vowels:

		word = word.replace(word[0], '')
		new_word = word + 'ay'
		print(new_word)

	else:

		last_letter = word[0]
		word = word.replace(word[0], '')
		new_word = word + last_letter + 'ay'
		print(new_word)

def multiple_translate(words):

	for word in words:

		single_translate(word)

pick_word()