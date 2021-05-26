#
#
#print grid

def columntops(c_num_in):
    initial = "+----+"
    addl = "----+"
    print(initial + (addl * c_num_in))

def sidelines(c_num_in):
    initial = "|    |"
    addl = "    |"
    print(initial + (addl * c_num_in))
    print(initial + (addl * c_num_in))
    print(initial + (addl * c_num_in))
    print(initial + (addl * c_num_in))


def printmain():

    print("""
          Hello, this is a grid printer.
          Please enter how many columns and
          rows you would like.
          """)

    column_in = int(input("Columns: "))
    column_in -=1
    rows_in = int(input("Rows: "))


    for n in range(rows_in):
        columntops(column_in)
        sidelines(column_in)
    print("+----+" + ("----+" * column_in))

again = 'y'

while (again=='y'):
    printmain()
    print("\n\n Would you like to print another? y = yes n = no")
    again = input("> ")






