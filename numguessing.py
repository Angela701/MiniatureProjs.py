# importing a random module
import random

# printing the starting & ending points of random numbers range
# r = random.randrange(-6, 12)
# print(r)

number = input("Type a number: ")

# if-else statement 
if number.isdigit():
    number = int(number)   # converting string into a integer

    if number <= 0:
        print("Please type a number greater than 0 next time.")
        quit()

else:
        print("Please type a number next time.")
        quit()

random_number = random.randint(0, number)
guesses = 0    # track how many guesses are made 

# printing the starting & ending point of random numbers (includ. end point)
# this would include "10"
# x = random.randint(-2, 10) 
# print (x)


# while loop condition statement 
while True:
    guesses += 1    # guesses from 1,2 etc. 
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)  # converting string to an integer 
    else:
        print("Please type a number next time.")
        continue    # "continue" brings back to top of loop

    if user_guess == random_number:   # equal-to statement 
        print("You got it!")
        break       # "break" immediately stops the loop          
    elif user_guess > random_number:   # greater than statement 
            print("You were above the number!")
    else:                           # less than statement 
            print("You are below the number!")

print("You got it in", + guesses, "guesses!")


    

