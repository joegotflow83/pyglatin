#!/usr/bin/env python3.5


def begin():

	choice = input("Do you want to [P]ig a word or [U]npig a word "
				 "Type a letter in the brackets: ").lower()

	if choice == 'p':

		pig_word()

	elif choice == 'u':

		unpig_word()

	else:

		print("I am sorry, what did you say? Type either p or u   ")
		begin()

def pig_word():

	pick_pig_word()

def unpig_word():

	pick_unpig_word()

def single_translate(word):

	vowels = ['a', 'e', 'i', 'o', 'u']

	if word[0] in vowels:

		word = word.replace(word[0], '')
		new_word = word + 'say'
		print(new_word)

	else:

		first_letter = word[0]
		word = word.replace(word[0], '')
		new_word = word + last_letter + 'ay'
		print(new_word)

def multiple_translate(words):

	for word in words:

		single_translate(word)

def single_reverse(word):

	new_word = word[0:(len(word) -2)]
	last_letter = new_word[-1]
	new_word = new_word.replace(new_word[-1], '')
	new_word = last_letter + new_word
	print(new_word)

def multiple_reverse(words):

	for word in words:

		single_reverse(word)

def pick_pig_word():

	word = input("Type a word to pig out: ")

	word = word.split(' ')
	
	if len(word) == 1:

		word = ''.join(word)
		single_translate(word)

	else:

		multiple_translate(word)

def pick_unpig_word():

	word = input("Type a word to unpig out: ")

	word = word.split(' ')
	
	if len(word) == 1:

		word = ''.join(word)
		single_reverse(word)

	else:

		multiple_reverse(word)

begin()