import random

print("Welcome to hangman")
print("**********")

wordDictionary = ["absurd", "larynx", "lymph", "crypt", "embezzle", "espionage", "fixable", "funny", "galaxy", "ivory", "jockey", "jovial", "zephyr", "vortex", "tropez", "subway", "sphinx", "puzzle", "numbskull", "mnemonic", "mystify"]

### choose random word
randomWord = random.choice(wordDictionary)
for x in randomWord:
    print("_", end=" ")

    def print_hangman(wrong):
        if(wrong == 0):
            print("\n+----+")
            print("       |")
            print("       |")
            print("       |")
            print(" =======")
        elif(wrong == 1):
            print("\n+----+")
            print("O      |")
            print("       |")
            print("       |")
            print(" =======")
        elif(wrong == 2):
            print("\n+----+")
            print("O      |")
            print("|      |")
            print("       |")
            print(" =======")
        elif(wrong == 3):
            print("\n+----+")
            print("O      |")
            print("/|     |")
            print("       |")
            print(" =======")
        elif(wrong == 4):
            print("\n+----+")
            print("O      |")
            print(" /|\   |")
            print("       |")
            print(" =======")
        elif(wrong == 5):
            print("\n+----+")
            print("O      |")
            print(" /|\   |")
            print(" /     |")
            print(" =======")
        elif(wrong == 6):
            print("\n+----+")
            print("O      |")
            print(" /|\   |")
            print(" / \   |")
            print(" =======")

    def printWord(guessedLetters):
        counter = 0
        rightletters = 0

    for char in randomWord:
        if(char in randomWord):
            counter = 0
            print(randomWord[counter], end=" ")
            rightletters = 0
            rightletters += 1
        else:
            print(" ", end=" ")
            counter += 1

    def print_lines():
        print("\r")

    for char in randomWord:
        print("\u203E", end=" ")

    length_of_word_to_guess = len(randomWord);
    amount_of_times_wrong = 0
    current_guess_index = 0
    current_letters_guessed =[]
    current_letters_right = 0

    ### Letters guessed
    while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
        print("\nLetters guessed:", end=" ")
        for letter in current_letters_guessed:
            print(letter, end=" ")

    ### Prompt user for input
    letterGuessed = input("\nGuess a letter: ").lower()

    ### User is right
    if(randomWord[current_guess_index] == letterGuessed):
        print_hangman(amount_of_times_wrong)

    ### Print word
    current_guess_index += 1
    current_letters_guessed.append(letterGuessed)
    current_letters_right = printWord(current_letters_guessed)
    print_lines()

    ### User is wrong
    amount_of_times_wrong += 1
    current_letters_guessed.append(letterGuessed)

    ### Update drawing
    print_hangman(amount_of_times_wrong)

    ### Print word
    current_letters_right = printWord(current_letters_guessed)
    print_lines()

    print("Game over! Thank you for playing :)")
