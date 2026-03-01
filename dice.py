import random 

print("Welcome to Dice Roll Game")

score = 0

while True:

    user = input("Enter S to start the game or Q to exit the game: ").lower().strip()

    if user == "s":
        dice = random.randint(1,6)
        print("You rolled:", dice)

        if dice == 6:
            print("u got 6. +1 point")
            score += 1
        else:
            print("u did not get 6, try again")

        print("ur total score:", score)

    elif user == "q":
        print("Game over")
        print("ur total and final score:", score)
        print("Thank u for playing")
        break

    else:
        print("Invalid input! Press S or Q only.")
