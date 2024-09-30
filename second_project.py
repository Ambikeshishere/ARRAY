# Rock Paper Scissor game
import random

choice_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move ( Rock, Paper, Scissor) \n >>>")
pc_choice = random.choice(choice_list)

print(f"User choice = {user_choice}\nComputer Choice ={pc_choice}")

if user_choice == pc_choice:
    print("DRAW")

elif user_choice == "Rock":
    if pc_choice == "Paper":
        print("Oh Sad, You lose......\n:-(")
    else:
        print("You win............\n:-)")

elif user_choice == "Paper":
    if pc_choice == "Scissor":
        print("Oh Sad, You lose......\n:-(")
    else:
        print("You win............\n:-)")

elif user_choice == "Scissor":
    if pc_choice == "Rock":
        print("Oh Sad, You lose......\n:-(")
    else:
        print("You win............\n:-)")