import random

number_range = []

create_range = int(input('Guessing range: '))
for n in range(create_range + 1):
    number_range.append(n)

random_number = random.choice(number_range)
restart = True

while restart:
    guess = int(input('Enter a number: '))

    if guess == random_number:
        print('Awsome!!! you guessed right')
        break

    elif guess > len(number_range[1:11]):
        print('Guess too high. Try again')
    elif guess < 0:
        print('Guess too low. Try again')
    else:
        print('Try again')
