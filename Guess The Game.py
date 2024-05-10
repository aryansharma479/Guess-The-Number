import random

def playgame():
    logo= ''' █▓▒▒░░░ GUESS THE GAME ░░░▒▒▓█'''.center(50)
    print(logo,'\n')
    print("Welcome To The Number Guessing Game !")
    print("***************************************")
    #number between 1 and 100
    print("I am thinking of a number between 1 and 100.")
    difficulty=input("Enter a difficulty level . Type 'easy','medium' or 'hard': ").lower()
    number=random.randint(1,100)
    #print(number)
    if difficulty=='easy':
        rightguess=False
        attempts=12
        while not rightguess and attempts !=0:
            print(f"You have {attempts} attempts remaining to guess the number. ")
            userguess=int(input("Make a guess: "))
            attempts-=1
            if attempts==0:
                    print("You have run out of attempts. 🤫")
            elif(userguess==number):
                print(f"Congratulations you have made a right guess ! 😊\nThe number is {number}. ")
                rightguess=True
            elif(userguess>number):
                print("Sorry ! Too High.😩")
                
            elif(userguess<number):
                print("Haha! Too Low.😩")

    elif difficulty=='medium':
        rightguess=False
        attempts=10
        while not rightguess and attempts !=0:
            print(f"You have {attempts} attempts remaining to guess the number. ")
            userguess=int(input("Make a guess: "))
            attempts-=1
            if attempts==0:
                    print("You have run out of attempts. 🤫")
            elif(userguess==number):
                print(f"Congratulations you have made a right guess ! 😊\nThe number is {number}. ")
                rightguess=True
            elif(userguess>number):
                print("Sorry ! Too High.😩")
                
            elif(userguess<number):
                print("Haha! Too Low.😩")
        
    elif difficulty=='hard':
        rightguess=False
        attempts=5
        while not rightguess and attempts !=0:
            print(f"You have {attempts} attempts remaining to guess the number. ")
            userguess=int(input("Make a guess: "))
            attempts-=1
            if attempts==0:
                    print("You have run out of attempts. 🤫")
            elif(userguess==number):
                print("Congratulations you have made a right guess ! 😊")
                rightguess=True
            elif(userguess>number):
                print("Sorry ! Too High.😩")
                
            elif(userguess<number):
                print("Haha! Too Low.😩")
    else:
        print("You have selected a wrong difficulty. Please Check Again")
    again=input('''Do You Want To Play The Game Again?
                    Type 'y' for yes and 'n' for no: ''').lower()
    while again=='y':
        playgame()
    if again=='n':
            exit()
playgame()                                                                                                           
