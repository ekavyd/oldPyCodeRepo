#
#
# Contacts app

class Contacts():
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        
        
###########################  ADD CONTACT F(X)  ##############################

def add_contact():

    print("\nYou selected: Add contact")
    print(" Please enter the full name of the contact: ")
    c_name = input("> ")
    c_mod_name = c_name.lower()

    print("\n Please enter the address of the contact: ")
    c_addr = str(input("> "))

    print("\n Please enter the phone number of the contact (no spaces or dashes): ")
    c_phone = str(input("> "))



# ....create key & enter class in dict

    new_entry = len(contactDB)
    new_entry_ref = str(c_mod_name)+ " - " + str(new_entry)

    contactDB[(str(new_entry_ref))] = Contacts(c_name, c_addr, c_phone)
    
    
    
    
    pauseVar = input("\nPRESS ENTER TO CONTINUE... ")
    return

##############################  SEARCH F(X)  #############################

def search_contact():

    print("\n You selected: Search for contact.")
    print(" Please enter the name you would like to search for: ")
    c_srch = input("> ")
    c_mod_srch = c_srch.lower()
    c_results = []




#....Look through the dictionary for matches

    for k, v in contactDB.items():
        if c_mod_srch in k :
            c_results.append(k)


#....print results

    for i in range(len(c_results)):
        tempname=c_results[i]
        
        print ("\n")
        print ((contactDB[tempname]).name)
        print ((contactDB[tempname]).address)
        print ((contactDB[tempname]).phone)
        print ("\n")


    print("\nPlease press enter when you are ready to return to the main menu")
    input(" ")




###############################  MAIN F(X)  #################################

def main():
    global contactDB
    contactDB = {}
    c_opt = 0

    while (c_opt != 3):
        print(''' \n\nHello, this is a small contacts manager app.
        Please select one of the following:

1. Add new contact
2. Find existing contact
3. Exit App
        ''')

        c_opt = int(input("> "))

        if c_opt == 1:
            add_contact()
        elif c_opt == 2:
            search_contact()
        elif c_opt == 3:
            print("\nGoodbye\n\n")
        else:
            print("That is not a valid option")


########################  MAIN BODY  ##################################

main()





