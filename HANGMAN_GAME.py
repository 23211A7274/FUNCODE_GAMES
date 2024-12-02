import random
import wordslist

# List of possible words for the game

def choose_word():
    """Randomly selects a word from the word list."""
    return random.choice(wordslist.word_list)

def display_word(word, guessed_letters):
    """Displays the current state of the word with guessed letters."""
    return ''.join([letter if letter in guessed_letters else ' _' for letter in word])

def hangman():
    # Choose a random word
    word = choose_word()
    guessed_letters = []  # To store the letters guessed so far
    incorrect_guesses = 0  # To keep track of incorrect guesses
    max_incorrect_guesses = 6  # Limit on incorrect guesses
    
    print("Welcome to Hangman!")
    print("Try to guess the word. You have", max_incorrect_guesses, "incorrect guesses.")
    
    # Game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the word
        print("Word:", display_word(word, guessed_letters))
        
        # Get the player's guess
        guess = input("Guess a letter: ").lower()

        # Check if the guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guess is correct
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! The letter '{guess}' is not in the word. You have {max_incorrect_guesses - incorrect_guesses} attempts left.")
        
        # Check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        # If the loop ends due to incorrect guesses limit being exceeded
        print(f"Game over! The correct word was: {word}")

# Run the game
if __name__ == "__main__":
    hangman()
