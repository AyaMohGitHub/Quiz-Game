
print(" Welcome to my Computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay lets play")
score = 0

answer = input(" What does CPU Stand for? ")

if answer.lower() == "central processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect!')

answer = input(" What does GPU Stand for? ")

if answer.lower() == "graphics processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect!')

answer = input(" What does RAM Stand for? ")

if answer.lower() == "random access memory":
    print('Correct')
    score += 1
else:
    print('Incorrect!')


answer = input(" What does PSU Stand for? ")

if answer.lower() == "power supply":
    print('Correct')
    score += 1
else:
    print('Incorrect!')


print("You got " + str(score) + "questions correct!")
print("You got " + str((score /4) * 100) + "%.")
