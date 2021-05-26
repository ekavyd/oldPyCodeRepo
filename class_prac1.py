#
#
#

class Contact:
    pass

x= Contact()
x.name = 'test name'

contacts=[]  #to hold all contacts profiles/instances


#----------------------CREATE CONTACT ------------------

def new_contact():
    '''
    Reads in a new contact and stores it
    '''
    print('Create a new contact')

    new_contact=Contact()
    new_contact.name = input(" Enter the contact's name: ")
    new_contact.address = input("Enter the contact's address: ")
    new_contact.telephone = input("Enter the contact's phone number: ")

    contacts.append(new_contact)

# a function to create new instances of the new class 'Contact'

#-------------------------------FIND CONTACT-----------
def find_contact():
    '''
    Reads in a name to search for a contact
    '''
    print("Find Contact")

    search_name = input("Enter the contact name: ")
    search_name = search_name.strip()  #remove whitespaces?
    search_name = search_name.lower() # all lower case

    result=None
    for contact in contacts:
        name = contact.name
        name=name.strip
        name = name.lower

        if name.startswith(search_name):
            result = contact
            break

    if result != None:
        print("Name: ", result.name)
        print("Address: ", result.address)
        print("Telephone: ", result.telephone)
    else:
        print("This name was not found")







