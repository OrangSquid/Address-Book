import json
import sys
from AddressBookCollections import *

def main():
    with open("contacts.json", "r") as file:
       contacts = json.load(file)
    
    # Asks the user his name if the name isn't known
    if contacts["user name"] == "":
        contacts["user name"] = input("Hello there! What's your name?")
        print("\nWelcome to your adress book, {}! What do you want do?".format(contacts["user name"]))
    else:
        print("\nWelcome to your adress book, {}! What do you want do?".format(contacts["user name"]))

    # Asks the user for an action to peform
    while True:
        action = input("""
    1. Check your Address Book
    2. Check a contact
    3. Add a new contact
    4. Modify a contact
    5. Delete a contact
    6. Exit and save\n\n""")

        # Checks the user input. If it is not a number from the list, it will ask him again
        while action != "1" and action != "2" and action != "3" and action != "4" and action != "5" and action != "6":
            action = input("You must input a number: ")

        # Starts doing the operation
        # Check Adress Book
        if action == "1":
            print_address_book()
        
        # Check a contact
        elif action == "2":
            temp = input("What's the contact name you're looking for?")
            search(temp)
        
        # Add a new contact
        elif action == "3":
            temp = {"name": input("What's his name? "),
                    "email": input("What's his email? "),
                    "phone number": input("What's his phone number? ")}
            contacts["contacts"].append(temp)
            del temp
            with open("contacts.json", "w") as f:
                json.dump(contacts, f)
        
        # Modify a contact
        elif action == "4":
            print_address_book()
            temp = input("What contact do you want to modify? Please input its name ")
            if print_contact(temp):
                modify = input("""What do you want to modify?
    1. Name
    2. Phone number
    3. Email\n\n""")
                while modify != "1" and modify != "2" and modify != "3":
                    modify = input("You must input a number between 1 and 3!")
                if modify == "1":
                    modifying = input("What's the new name?")
                    modifyer(temp, "name", modifying)
                elif modify == "2":
                    modifying = input("What's the new phone number?")
                    modifyer(temp, "phone number", modifying)
                else:
                    modifying = input("What's the new email?")
                    modifyer(temp, "email", modifying)
            else:
                print("There's no such contact!")
        
        # Delete a contact
        elif action == "5":
            temp = input("What's the name of the contact you want to delete?")
            delete(temp)
        
        # Exit
        else:
            input("Press Enter to exit . . .")
            with open("contacts.json", "w") as f:
                json.dump(contacts, f)
            sys.exit()

if __name__ == "__main__":
    main()