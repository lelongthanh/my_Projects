import random

options = ['paper', 'rock', 'scissor']
playing = True

while playing:
    print('===Welcome to the game===')

    player = input("Enter (paper/rock/scissor): ")
    AI = random.choice(options)

    while True:
        if (player==AI):
            print(f"PlayervsAI: {player} = {AI}. We\'re all good")
            break
            
        elif (player!=AI):
            if (player=='paper') and (AI=='rock'):
                print(f"PlayervsAI: {player} > {AI}. YOU WIN!!")
            elif (player=='rock') and (AI=='scissor'):
                print(f"PlayervsAI: {player} > {AI}. YOU WIN!!")
            elif (player=='scissor') and (AI=='paper'):
                print(f"PlayervsAI: {player} > {AI}. YOU WIN!!")
            else:
                print(f"PlayervsAI: {player} < {AI}. YOU LOSE!!")
            break
                          
        else:
            print("Invalid value")
            break

    tryAgain = input("Try again? (y/n): ")
    if tryAgain.lower() == 'n':
        playing = False
print("Thanks for playing")


    
  
        