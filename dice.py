import random
print("welcome to the dice roll game!")


while True:
   
    user = input("press R to enter the game and press Q to exit the game\n:").lower().strip()
    dice_unknow = random.randint(1,6)
    if user == "r":
        print("u rollerd a dice:",dice_unknow)



        if dice_unknow == "6":
            print("You got a six! Congratulation!")
        else:
            print("Roll the dice again to try your luck!")
    

    elif user == "q":
        print("thanku for playing good bye!!")


    

    
    


   
