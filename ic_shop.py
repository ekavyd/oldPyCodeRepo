#
#
#
##------------------------MAIN SELECTION INTRO------------------------------

def main():
    global storelist
    global incomelist
    storelist = ['store1' 'store2', 'store3', 'store4', 'store5']
    incomelist = float[0.0, 0.0, 0.0, 0.0, 0.0]
    while (usr_sel != 8):
        print("""\n\n  Hello, this is a sale report manager.
        Please select an option:
        1- Print the sales
        2- Sort/Print sales High to Low
        3- Sort/Print sales Low to High
        4- Print Highest and Lowest only
        5- Print Total Sales
        6- Print Avg Sales
        7- Enter sales data
        8- Quit Program
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




##--------------------------INPUT SALES DATA--------------------------

def input_sales():
    print(" Which shop would you like to input sales data for?")
    print(f"1- {global.storelist[0]}  ")
    print(f"2- {global.storelist[1]}  ")
    print(f"3- {global.storelist[2]}  ")
    print(f"4- {global.storelist[3]}  ")
    print(f"5- {global.storelist[4]}  ")
    print(f"6- New Store  ")

    shop_num = int(input("> "))

    if shop_num == 6:
        addshop()

    shop_num -=1
    print(f"Please input the sales data for {global.storelist[shop_num]} in dollars.")
    sales_amt = float(input("$ "))

    incomelist[shop_num] = sales_amt


##---------------------------ADDING SHOP----------------------------

def addshop():
    i_num = len(storelist)
    act_num = i_num +1
    storelist[i_num] = 'Store' + str(ac_num)


##--------------------------PRINTING SALES------------------------

def printsales():
    for i in range(len(storelist)):
        print(f" {global.storelist[i]}  ${global.incomelist[i]} ")

##--------------------------------------------------------------------




#printsales, sortHL, sortLH, HL only, totalsales, avgsales, enter sales, quit


main()












