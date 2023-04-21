#!/usr/bin/env python3

import random

print("Welcome to hangman")
print("********************")

wordDictionary = ["apple, orange, banana, kiwi, strawberry, raspberry, blueberry, blackberry, cherry, peach, plum, pear, watermelon, cantaloupe, honeydew, grapefruit, lemon, lime, grape, pineapple, coconut, mango, papaya, avocado, broccoli, carrot, cauliflower, tomato, potato, onion, garlic, pepper, cucumber, lettuce, spinach, kale, zucchini, squash, mushroom, asparagus, celery, radish, turnip, beet, parsnip, rutabaga, cabbage, eggplant, artichoke, okra, aspen, maple, oak, pine, birch, cedar, cypress, elm, fir, juniper, willow, hickory, poplar, walnut, acorn, feather, fur, leather, wool, silk, cotton, denim, linen, lace, velvet, satin, polyester, nylon, rubber, plastic, metal, gold, silver, copper, iron, steel, aluminum, titanium, bronze, nickel, zinc, cobalt, mercury, helium, neon, argon, krypton, xenon, radon, hydrogen"]

### Choose random word
randomword = random.choice(wordDictionary)

for x in randomword:
print("_", end=" ")

def print_hangman (wrong):
	if(wrong == 0 ):
		print("\n+----+")
		print("      |")
		print("      |")
		print("      |")
		print("     ===")
	elif(wrong == 1):
		print("\n+----+")
		print("O     |")
		print("      |")
		print("      |")
		print("     ===")
	elif(wrong == 2):
		print("\n+----+")
		print("O     |")
		print("|     |")
		print("      |")
		print("     ===")
	elif(wrong == 3):
		print("\n+----+")
		print("O     |")
		print("/|    |")
		print("      |")
		print("     ===")
	elif(wrong == 4):
		print("\n+----+")
		print("O     |")
		print("/|\   |")
		print("      |")
		print("     ===")
	elif(wrong == 5):
		print("\n+----+")
		print("O     |")
		print("/|\   |")
		print("/     |")
		print("     ===")
	elif(wrong == 6):
		print("\n+----+")
		print("O     |")
		print("/|\   |")
		print("/ \   |")
		print("     ===")

def printWord(guessedLetters):
	counter = 0
	rightLetters = 0
	for char in randomWord:
	if(char in guessedLetters):
		print(randomWord[couner], end=" ")
		rightLetters+=1
	else:
	 print(" ", end=" ")
	 counter+=1
	return rightLetters

def print_lines():
	print("\r")
	for char in randomWord:
	print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
	print("\nLetters guessed so far: ")
	for letter in current_letters_guessed:
	print(letter, end=" ")
### Prompt for user input
	letterGuessed = input("\nGuess a letter: ")
### User is right
	if(randomWord[surrent_guess_index] == letterGuessed):
		print_hangman(amount_of_times_wrong)
### Print word
	current_guessed_index+=1
	current_letters_guessed.append(letterGuessed)
	current_letters_right = printWord(current_letter_guessed)
	printLines()
### User is wrong
	else:
	amount_of_times_wrong+=1
	current_letters_guessed.append(letterGuessed)
### Update drawing
	print_hangman(amount_of_times_wrong)
### Print word
	current_letters_right = printWord(current_letter_guessed)
	printLines()

print("Game over! Thank you for playing :)")
