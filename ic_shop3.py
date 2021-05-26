#
#
#
##------------------------MAIN SELECTION INTRO------------------------------

from operator import itemgetter
import os.path

def main():
    global storelist
    global incomelist
    storelist = ['store1', 'store2', 'store3', 'store4', 'store5']
    incomelist = [0.0, 0.0, 0.0, 0.0, 0.0]
    usr_sel = 0
    while (usr_sel != 11):
        print("------------------- \n")
        print("""\n\n  Hello, this is a sale report manager.
        Please select an option: \n
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
            temp_store, temp_income = load_data()
            storelist.clear()
            incomelist.clear()
            storelist=temp_store
            incomelist= temp_income




##--------------------------INPUT SALES DATA--------------------------

def input_sales():
    print(" Which shop would you like to input sales data for? \n")

    for i in range(len(storelist)):
        print(f" {i} - {storelist[i]}  ")
   # print(f"2- {storelist[1]}  ")
   # print(f"3- {storelist[2]}  ")
   # print(f"4- {storelist[3]}  ")
   # print(f"5- {storelist[4]}  ")


    print(f"99- New Store  ")

    shop_num = int(input("> "))

    if shop_num == 99:
        shop_num = addshop()
        #shop_num += 1

    shop_num -=1
    print(f"Please input the sales data for {storelist[shop_num]} in dollars.")
    sales_amt = float(input("$ "))

    incomelist[shop_num] = sales_amt


##---------------------------ADDING SHOP----------------------------

def addshop():
    print("------------------- \n")
    i_num = len(storelist)
    #act_num = i_num +1
    storelist.append('Store' + str(i_num+1))
    incomelist.append(0.0)
    return (len(storelist))


##---------------------------RENAME SHOP----------------------------

def rename_shop():
    print("------------------- \n")
    print("What shop would you like to rename?")
    for i, name in enumerate(storelist):
        print(f" {i+1}. {storelist[i]} ")

    s_sel = int(input("> "))
    s_sel -= 1
    new_name= input("New Storename: ")
    storelist[s_sel] = new_name

##--------------------------PRINTING SALES------------------------

def print_sales():
    print("------------------- \n")
    for i in range(len(storelist)):
        print(f" {storelist[i]}      \t ${incomelist[i]} ")


##--------------------------PRINTING High to Low------------------

def sort_HL():
    print("------------------- \n")
    templist=(sorted(zip(storelist, incomelist), key=itemgetter(1), reverse=True))
    for i, entry in enumerate(templist):
        print(f"{i+1}. {templist[i]}")

##--------------------------PRINTING Low to High------------------

def sort_LH():
    print("------------------- \n")
    templist=sorted(zip(storelist, incomelist), key=itemgetter(1))
    for i, entry in enumerate(templist):
        print(f"{i+1}. {templist[i]}")

##--------------------------PRINTING High and Low Only-----------

def HL_only():
    print("------------------- \n")
    templist=sorted(zip(storelist, incomelist), key=itemgetter(1))
    low_store=templist[0]
    high_store=templist[(len(templist)-1)]
    print(f"Lowest Sales: {low_store} \nHighest Sales:{high_store}")

##--------------------------PRINTING Total Sales----------------

def total_sales():
    print("------------------- \n")
    sum_sales=0.0
    for i in range(len(incomelist)):
        sum_sales = sum_sales + incomelist[i]
    print(f"Total Sales Revenue: {sum_sales}")

##--------------------------Average Sales----------------------

def avg_sales():
    print("------------------- \n")
    avg_sales=0.0
    for i in range(len(incomelist)):
        avg_sales = avg_sales + incomelist[i]
    avg_sales = avg_sales / (len(storelist))
    print(f"Average Sales Revenue: {avg_sales}")


##--------------------------Save Data-------------------------


def save_data():
    print("------------------- \n")
    print("What would you like to name the data file?")
    name_sel = input("> ")

    name_sel = (name_sel + ".txt")
    print(name_sel)

    data_src= open(name_sel, 'w')

    t_storelist =[]
    t_incomelist =[]
    t2_incomelist =[]



    t_storelist = ','.join(storelist)
    t_storelist = t_storelist + '\n'


    for i in range(len(incomelist)):
        t_incomelist.append(str(incomelist[i]))

    t2_incomelist = ','.join(t_incomelist)
    t2_incomelist = t2_incomelist + '\n'

    data_src.write(t_storelist)
    data_src.write(t2_incomelist)


    data_src.close()

##--------------------------Load Data-------------------------


def load_data():
    print("------------------- \n")
    file_list = os.listdir()
    for item in file_list:
        print(item)    #list of everything in current directory

    print("What is the name the data file?")
    name_sel = input("> ")
    if os.path.isfile(name_sel): #test to see if file exists
        data_src = open(name_sel, 'r')
    else:
        return

    t_storelist = data_src.readline()
    t_storelist = t_storelist.rstrip()
    storelist = t_storelist.split(",")

    t_incomelist = data_src.readline()
    t_incomelist = t_incomelist.rstrip()
    incomelist = t_incomelist.split(",")

    data_src.close()

    return(storelist, incomelist)




##--------------------------Gen Body-------------------------
# error code


main()












