print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:)")

score=0

answer  = input("What does CPU stand for? ")
if answer.lower() == "central processing unit" : 
    print('Correct!')
    score += 1 
else: 
    print("Incorrect!")


answer  = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit" : 
    print('Correct!')
    score += 1 
else: 
    print("Incorrect!")


answer  = input("What does RAM stand for? ")
if answer.lower() == "Random Access Memory" : 
    print('Correct!')
    score += 1 
else: 
    print("Incorrect!")

answer  = input("What does PSU stand for? ")
if answer.lower() == "Power Supply" : 
    print('Correct!')
    score += 1   
else: 
    print("Incorrect!")


print("You got {} questions correct".format((score/4)*100))
# answer  = input("What does  stand for? ")




