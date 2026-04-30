"""
Task 4: Closure Practice
    Within the assignment3 folder, create a file called hangman-closure.py.
    Declare a function called make_hangman() that has one argument called secret_word. It should also declare an empty array called guesses. Within the function declare a function called hangman_closure() that takes one argument, which should be a letter.
    Within the inner function, each time it is called, the letter should be appended to the guesses array. Then the word should be printed out, with underscores substituted for the letters that haven't been guessed. 
    So, if secret_word is "alphabet", and guesses is ["a", "h"], then "a__ha__" should be printed out. The function should return True if all the letters have been guessed, and False otherwise. make_hangman() should return hangman_closure.
    Within hangman-closure.py, implement a hangman game that uses make_hangman(). Use the input() function to prompt for the secret word. Then use the input() function to prompt for each of the guesses, until the full word is guessed.
    Test your program by playing a few games.
"""

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        # Build the displayed word
        display = ""
        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"

        print(display)

        # Check if all letters have been guessed
        return all(char in guesses for char in secret_word)

    return hangman_closure


if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").lower()
    game = make_hangman(secret_word)

    print("\nStart guessing!")

    while True:
        guess = input("Guess a letter: ").lower()

        if not guess or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        is_complete = game(guess)

        if is_complete:
            print(f"You guessed it! The word was '{secret_word}'")
            break