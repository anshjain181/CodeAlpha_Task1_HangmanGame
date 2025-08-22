import random

# Predefined list of words
words = ["apple", "house", "chair", "table", "plant"]

# Choose a random word from the list
word = random.choice(words)
word_letters = set(word)  # unique letters in the word
guessed_letters = set()   # letters guessed by the player
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print("_ " * len(word))  # show blank spaces for the word

# Game loop
while incorrect_guesses < max_incorrect and word_letters:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single letter.")
                continue

        if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

        guessed_letters.add(guess)

        if guess in word_letters:
                word_letters.remove(guess)
                print("Correct!")
        else:
                incorrect_guesses += 1
                print(f"Wrong! You have {max_incorrect - incorrect_guesses} guesses left.")

        # Display current progress
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display_word))

# End of game
if not word_letters:
        print(f"Congratulations! You guessed the word '{word}'!")
else:
        print(f"Game over! The word was '{word}'.")