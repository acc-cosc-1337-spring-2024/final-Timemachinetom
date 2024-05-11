import question_d
from question_d import create_multiplication_table

exit = 0
quit = False

while quit != True:
    table = question_d.create_multiplication_table ()
    question_d.display_multiplication_table (table)
    exit = input ("\n\nWould you like to see the multiplication table again?\n1 - Yes\n2 - Quit\n")
    exit = int(exit)
    if exit == 2:
        sure = input ("Are you sure you want to exit?\n1 - Yes\n2 - No\n")
        sure = int(sure)
        if sure == 1:
            exit = 0
            print("Goodbye")
            quit = True
        elif sure == 2:
            sure = 0
            exit = 0
        else:
            sure = 0
            exit = 0







