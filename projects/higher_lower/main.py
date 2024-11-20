from game_data import data
import random

def higher_lower_game():
    should_continue = True
    score = 0
    acc_b = random.choice(data)
    while should_continue:
        # after comparing, acc_b will replace acc_a and generate a new random data
        acc_a = acc_b
        acc_b = random.choice(data)
        # compare with another acc_b to make sure acc_a and acc_b are not the same infor
        if acc_a == acc_b:
            acc_b = random.choice(data)

        print(f"Compare A: {acc_a["name"]}, a {acc_a["description"]}, from {acc_a["country"]}.")
        print(f"Against B: {acc_b["name"]}, a {acc_b["description"]}, from {acc_b["country"]}.")

        answer = input("Who has more followers? type 'A' or 'B': ").upper()
        # check if followers of acc_a > acc_b
        acc_a_followers = acc_a["follower_count"]
        acc_b_followers = acc_b["follower_count"]

        if answer == 'A':
            if acc_a_followers > acc_b_followers:
                score += 1
                print(f"You're right. Current score: {score}")
            else:
                print("\n" * 100)
                print(f"That's wrong. Final score: {score}")
                should_continue = False
        # check if followers of acc_b > acc_a
        elif answer == 'B':
            if acc_b_followers > acc_a_followers:
                score += 1
                print(f"You're right. Current score: {score}")
            else:
                print("\n"*100)
                print(f"That's wrong. Final score: {score}")
                should_continue = False

higher_lower_game()