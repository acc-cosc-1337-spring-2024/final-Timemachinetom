#add import
import question_b
from question_b import Stock

option = 0
quit = False

while quit != True:
    option = input ("Question B Menu\n1-Display Stock Purchase History\n2-Exit\n")
    option = int(option)

    if option == 1:
        question_b.stock_purchase_history()
        exit = input ("Do you want to exit?\n1 - Yes\n2 - No\n")
        exit = int(exit)
        if exit == 1:
            exit = 0
            option = 0
            sure = input ("Are you sure you want to exit?\n1 - Yes\n2 - No\n")
            sure = int(sure)
            if sure == 1:
                exit = 0
                option = 0
                print("Goodbye")
                quit = True
            elif sure == 2:
                sure = 0
                exit = 0
                option = 0
            else:
                sure = 0
                exit = 0
                option = 0
        elif exit == 2:
            exit = 0
            option = 0 
        else:
            exit = 0
            option = 0
    if option == 2:
        exit = input ("Are you sure you want to exit?\n1 - Yes\n2 - No\n")
        exit = int(exit)
        if exit == 1:
            exit = 0
            option = 0
            print("Goodbye")
            quit = True
        elif exit == 2:
            exit = 0
            option = 0
    else:
        option = 0