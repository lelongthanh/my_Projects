import random

answer = random.choice(range(1,101))
easy_attempts = 10
hard_attempts = 5

def easy_level(number):
    """ Easy mode have 10 attempts and compare guess numb with answer """
    global easy_attempts
    if number > answer:
        easy_attempts -= 1
        print("Too high. Guess again")
        print(f"You have {easy_attempts} attempts remaining to guess a number")
    elif number < answer:
        easy_attempts -= 1
        print("Too low. Guess again")
        print(f"You have {easy_attempts} attempts remaining to guess a number")

def hard_level(number):
    """ Hard mode have 5 attempts and compare guess numb with answer """
    global hard_attempts
    if number > answer:
        hard_attempts -= 1
        print("Too high. Guess again")
        print(f"You have {hard_attempts} attempts remaining to guess a number")
    elif number < answer:
        hard_attempts -= 1
        print("Too low. Guess again")
        print(f"You have {hard_attempts} attempts remaining to guess a number")

def number_guessing_game():
    print("Welcome to the Number guessing game")
    print("I'm thinking of a number between 1 and 100")
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    guessing = True
    # repeat guessing number until guess it right
    while guessing:

        guess_a_number = int(input("Make a guess: "))

        if game_level == 'easy':
            easy_level(guess_a_number)

            if easy_attempts == 0:
                print("You've run out of guess. Refreshing the page to continue playing")
                guessing = False
        else:
            hard_level(guess_a_number)

            if hard_attempts == 0:
                print("You've run out of guess. Refreshing the page to continue playing")
                guessing = False

        if guess_a_number == answer:
            print(f"You guess right!!!. The answer is: {answer}")
            guessing = False

number_guessing_game()