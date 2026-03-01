import random 

print("welcome to dice roll game")

score = 0

while True:

    user = input("enter S to start the game or Q to exit the game:").lower().split()


    if user == "c":
        dice = random.randint(1,6)
        print("you rolled:",dice)
        if dice == 6:
            print("you got 6 meat +1 point")
            score += 1
        else:
            print("u did not got six try once again")

        print("ur total score:",score)

    elif user == "q":
        print("game over")
        print("ur total and final score:", score)
        print("thanku for playing")
        break
