import random

AI = ['paper', 'rock', 'scissor']
AI_random = random.choice(AI)

while True:
    print('===Welcome to the game===')

    player = input("Enter (paper/rock/scissor): ")

    if (player=='paper' and AI_random=='paper') or (player=='rock' and AI_random=='rock') or (player=='scissor' and AI_random=='scissor'):
        print(f"PlayervsAI: {player} = {AI_random}. We\'re all good")
        break

    elif (player=='paper') and (player!=AI_random):
        if (player=='paper') and (AI_random=='rock'):
            print(f"layervsAI: {player} > {AI_random}. Okay you WIN!!!")
            break
        elif (player=='paper') and (AI_random=='scissor'):
            print(f"layervsAI: {player} < {AI_random}. OOps wanna try again?!")
            break

    elif (player=='rock') and (player!=AI_random):
        if (player=='rock') and (AI_random=='scissor'):
            print(f"layervsAI: {player} > {AI_random}. Okay you WIN!!!")
            break
        elif (player=='rock') and (AI_random=='paper'):
            print(f"layervsAI: {player} < {AI_random}. OOps wanna try again?!")
            break

    elif (player=='scissor') and (player!=AI_random):
        if (player=='scissor') and (AI_random=='paper'):
            print(f"layervsAI: {player} > {AI_random}. Okay you WIN!!!")
            break
        elif (player=='scissor') and (AI_random=='rock'):
            print(f"layervsAI: {player} < {AI_random}. OOps wanna try again?!")
            break
        
    else:
        print("Invalid value")

    
  
        