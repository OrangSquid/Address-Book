# Fucntions to modify, print and check the adress book
# These functions are separate to make the main script more clean

import json

# Makes public variable to later use on modifyer
checked = ""

def check_contact_name(name):
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
    for x in contacts["contacts"]:
        if x["name"] == name:
            global checked
            checked = x
            return True
    return False

def print_address_book():
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
    for x in contacts["contacts"]: 
        print("Name: {}".format(x["name"]))
        print("Phone Number: {}".format(x["phone number"]))
        print("Email: {}\n".format(x["email"]))

def print_contact(name):
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
    for x in contacts["contacts"]:
        if x["name"] == name:
            print("\nName: {}".format(x["name"]))
            print("Phone Number: {}".format(x["phone number"]))
            print("Email: {}\n".format(x["email"]))
            return True
    return False

def modifyer(name, modify, result):
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
    for x in enumerate(contacts["contacts"]):
        if x[1]["name"] == name:
            x[1][modify] = result
            del contacts["contacts"][x[0]]
            contacts["contacts"].insert(x[0], x[1])
        with open("contacts.json", "w") as f:
            json.dump(contacts, f)

def search(name):
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
    if not print_contact(name):
        print("There's no such contact in your list.")

def delete(name):
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
    for x in enumerate(contacts["contacts"]):
        if x[1]["name"] == name:
            del contacts["contacts"][0]
            with open("contacts.json", "w") as f:
                json.dump(contacts, f)