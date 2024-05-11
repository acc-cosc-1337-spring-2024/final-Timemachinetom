
def create_multiplication_table ():
    table = []
    for column in range (1,6):
        for row in range (1,11):
            table.append (row*column)
    return (table)

def display_multiplication_table (table):
    go = True
    start = 0
    end = 10
    while go == True:
        row = []
        for i in range (start, end):
            row.append (table[i])
        print (*row)
        start += 10
        end += 10
        if start == 50:
            go = False