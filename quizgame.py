
# string 
print("Welcome to my quiz game!") 

# variable 
playing = input("Do you want to play? ")
print(playing)

# lower-upper case statement
if playing.lower() != "yes":
    quit()   #quit would immediately terminate the program
print("Okay! Let's play! " )

# using "score" to keep track of all the correct answers 
score = 0 

# if-else statement 
answer = input("____ is how we write code ").lower()
if answer == "syntax":
    print('Correct!')
    score += 1
    # score = score + 1 
else:
    print("Incorrect!")
    
    
answer = input("An algorithm that has been coded into something that can be run by a machine _____ ")
if answer.lower() == "program":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("______ is finding and fixing problems in a program ")
if answer.lower() == "debugging":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("What is a list of steps to complete a task? ")
if answer.lower() == "algorithm":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("___ is a memory where you store values. ")
if answer.lower() == "variable":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")



# converted score to a string since numbers and string cannot be used together 
print("You got " + str(score) + " questions correct!")

# percentage of correct answers
print("You got " + str((score/7) * 100) + "%") 
