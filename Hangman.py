import random
import string
from words import words  # This should be a list of words in a separate file named words.py

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:  # Space was an empty string before, corrected to a space
        word = random.choice(words)
    return word.upper()  # Return word in uppercase for consistency

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Unique letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters the user has guessed

    lives = 6  # Optional: number of lives

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Show used letters
        print('You have used these letters: ', ' '.join(sorted(used_letters)))
        # Show current word progress
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        print(f"Lives left: {lives}")

        # Get user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f'Good job! {user_letter} is in the word.')
            else:
                lives -= 1
                print(f'Sorry, {user_letter} is not in the word.')

        elif user_letter in used_letters:
            print('You already used that letter. Try again.')

        else:
            print('Invalid character. Please enter a letter.')

        print()  # Empty line for spacing

    # Game over
    if lives == 0:
        print(f'Sorry, you died. The word was {word}.')
    else:
        print(f'Yay! You guessed the word {word}!!')

# To start the game
if __name__ == '__main__':
    hangman()
