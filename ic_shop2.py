#
#
#
##------------------------MAIN SELECTION INTRO------------------------------

from operator import itemgetter

def main():
    global storelist
    global incomelist
    storelist = ['store1', 'store2', 'store3', 'store4', 'store5']
    incomelist = [0.0, 0.0, 0.0, 0.0, 0.0]
    usr_sel = 0
    while (usr_sel != 11):
        print("""\n\n  Hello, this is a sale report manager.
        Please select an option:
        1- Print the sales
        2- Sort/Print sales High to Low
        3- Sort/Print sales Low to High
        4- Print Highest and Lowest only
        5- Print Total Sales
        6- Print Avg Sales
        7- Enter sales data
        8- Rename Store
        9- Save Sales Data
        10- Load Sales Data
        11- Quit Program
        """)

        usr_sel = int(input("> "))

        if usr_sel ==1:
            print_sales()
        elif usr_sel==2:
            sort_HL()
        elif usr_sel==3:
            sort_LH()
        elif usr_sel==4:
            HL_only()
        elif usr_sel==5:
            total_sales()
        elif usr_sel==6:
            avg_sales()
        elif usr_sel==7:
            input_sales()
        elif usr_sel==8:
            rename_shop()
        elif usr_sel==9:
            save_data()
        elif usr_sel==10:
            load_data()




##--------------------------INPUT SALES DATA--------------------------

def input_sales():
    print(" Which shop would you like to input sales data for?")
    print(f"1- {storelist[0]}  ")   #need to change to for statement with enumerate for new store additions
    print(f"2- {storelist[1]}  ")
    print(f"3- {storelist[2]}  ")
    print(f"4- {storelist[3]}  ")
    print(f"5- {storelist[4]}  ")
    print(f"6- New Store  ")

    shop_num = int(input("> "))

    if shop_num == 6:
        addshop()

    shop_num -=1
    print(f"Please input the sales data for {storelist[shop_num]} in dollars.")
    sales_amt = float(input("$ "))

    incomelist[shop_num] = sales_amt


##---------------------------ADDING SHOP----------------------------

def addshop():
    i_num = len(storelist)
    act_num = i_num +1
    storelist[i_num] = 'Store' + str(act_num)


##---------------------------RENAME SHOP----------------------------

def rename_shop():
    print("What shop would you like to rename?")
    for i, name in enumerate(storelist):
        print(f" {i+1}. {storelist[i]} ")

    s_sel = int(input("> "))
    s_sel -= 1
    new_name= input("New Storename: ")
    storelist[s_sel] = new_name

##--------------------------PRINTING SALES------------------------

def print_sales():
    for i in range(len(storelist)):
        print(f" {storelist[i]}  ${incomelist[i]} ")

##--------------------------PRINTING High to Low------------------

def sort_HL():
    templist=(sorted(zip(storelist, incomelist), key=itemgetter(1), reverse=True))
    for i, entry in enumerate(templist):
        print(f"{i+1}. {templist[i]}")

##--------------------------PRINTING Low to High------------------

def sort_LH():
    templist=sorted(zip(storelist, incomelist), key=itemgetter(1))
    for i, entry in enumerate(templist):
        print(f"{i+1}. {templist[i]}")

##--------------------------PRINTING High and Low Only-----------

def HL_only():
    templist=sorted(zip(storelist, incomelist), key=itemgetter(1))
    low_store=templist[0]
    high_store=templist[(len(templist)-1)]
    print(f"Lowest Sales: {low_store} \nHighest Sales:{high_store}")

##--------------------------PRINTING Total Sales----------------

def total_sales():
    sum_sales=0.0
    for i in range(len(incomelist)):
        sum_sales = sum_sales + incomelist[i]
    print(f"Total Sales Revenue: {sum_sales}")

##--------------------------Average Sales----------------------

def avg_sales():
    avg_sales=0.0
    for i in range(len(incomelist)):
        avg_sales = avg_sales + incomelist[i]
    avg_sales = avg_sales / (len(storelist))
    print(f"Average Sales Revenue: {avg_sales}")


##--------------------------Save Data-------------------------


def save_data():
    print("What would you like to name the data file?")
    name_sel = input("> ")
    name_sel = (name_sel + ".txt")


##--------------------------Load Data-------------------------


def load_data():





##--------------------------Gen Body-------------------------
# error code


main()












