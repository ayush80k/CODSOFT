import random as rd

c_list = ['ROCK','PAPER','SCISSORS']

print("\nWelcome to a game of Rock, PAper and Scissors! \nThere are multiple rounds, the score is as folllows: \nWin: +2 points\nTie: +1 point to both\nLoss: -1 point\n")


u_scr = 0
c_scr = 0

flag = 0

while flag == 0:

    u_in = str(input("\nEnter your choice: Rock, Paper or Scissors - \n"))
    u_choice = u_in.upper()
    c_choice = rd.choice(c_list)

    if u_choice in c_list:

        print("\nYou: ",u_choice,"\tComputer: ",c_choice,"\n")

        if u_choice == 'ROCK':
            if c_choice == 'SCISSORS':
                print("You won!, +2 points")
                u_scr += 2
                c_scr -= 1

            elif c_choice == 'PAPER':
                print("You Lost!, -1 point")
                u_scr -= 1
                c_scr += 2
            
            elif c_choice == 'ROCK':
                print("It is a tie. +1 to both")
                u_scr += 1
                c_scr += 1

        elif u_choice == 'PAPER':
            if c_choice == 'ROCK':
                print("You won!, +2 points")
                u_scr += 2
                c_scr -= 1

            elif c_choice == 'SCISSORS':
                print("You Lost!, -1 point")
                u_scr -= 1
                c_scr += 2
            
            elif c_choice == 'PAPER':
                print("It is a tie. +1 to both")
                u_scr += 1
                c_scr += 1

        elif u_choice == 'SCISSORS':
            if c_choice == 'PAPER':
                print("You won!, +2 points")
                u_scr += 2
                c_scr -= 1

            elif c_choice == 'ROCK':
                print("You Lost!, -1 point")
                u_scr -= 1
                c_scr += 2
            
            elif c_choice == 'SCISSORS':
                print("It is a tie. +1 to both")
                u_scr += 1
                c_scr += 1


        print("\nTotal Scores:\nYou - ",u_scr,"\nComputer - ",c_scr)


        print("\nDo you want to continue? Type Yes or No.")
        cont = str(input("YES or NO - "))
        cont_u = cont.upper()
        if cont_u != 'YES':
            flag += 1
            print("\nFinal Result:  You ",u_scr,"\tComputer ",c_scr)
            if u_scr > c_scr:
               print("You Won!")
            elif u_scr < c_scr:
                print("You lost.")
            else:
                print("It is a Tie")

    else: 
        print("Enter a Valid Choice.")
        