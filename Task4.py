# Rock Paper Scissors Game
import random

print("Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user = input("Enter rock, paper, scissors or exit: ").lower()

    if user == "exit":
        print("Final Score -> You:", user_score, "Computer:", computer_score)
        break

    if user not in choices:
        print("Invalid choice")
        continue

    computer = random.choice(choices)

    print("You:", user)
    print("Computer:", computer)

    if user == computer:
        print("Tie")

    elif user == "rock" and computer == "scissors":
        print("You win")
        user_score += 1

    elif user == "paper" and computer == "rock":
        print("You win")
        user_score += 1

    elif user == "scissors" and computer == "paper":
        print("You win")
        user_score += 1

    else:
        print("Computer wins")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)