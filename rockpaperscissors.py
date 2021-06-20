# importing random module 
import random

# user_wins and computer_wins 
user_wins = 0
computer_wins = 0

# list index   0      1      2
options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
# if user didn't select rock,paper, or scissors -- "continue" to start over 
    if user_input not in options:
        continue

# if selected string is valid, then

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

# Deciding who won -- individual or computer 
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
      
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print(f" Both players selected {user_input}. It's a tie!")
        
    else:
        print("You lost!")
        computer_wins += 1
        
    
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")

print("Goodbye!")
