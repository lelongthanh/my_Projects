import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)

# create "_" as many as word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # lives remaining
    print(f"---{lives}/6 LIVES LEFT---")

    guess = input("Guess a letter: ").lower()
    display = ""

    # notify the word has already entered
    if guess in correct_letters:
        print(f"You\'ve already guessed: {guess}")

    # Guess the word. Display the word if the letter exist in the word
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"


    print("Word to guess: " + display)

    # Guess the word. deduct a life if the letter doesn't exist in the word
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that\'s not in the word. You lose a life")

        if lives == 0:
            game_over = True
            print(f"Correct word: {chosen_word}!")
            print(f"---YOU LOSE---")

    if "_" not in display:
        game_over = True
        print("!!!---YOU WIN---!!!")

    print(stages[lives])
