contact = {}

def display_contact():
    print("name\t\tcontact number")
    for key in contact:
        print("{}\t\t\t{}".format(key,contact.get(key)))


while True:
    choice = int(input("1.Add new contact \n 2. search contact \n3 .Display contact \n4.edit contact\n 5.delete contact\n 6. exit \n"))
    if choice == 1:
        name = input("enter your name")
        phone=input("enter your phone number\n")
        contact[name] = phone
    elif choice == 2:
        search_name = input("enter the contact name")
        if search_name in contact:
            print(search_name,"contact number is:-\n ",contact[search_name])
        else:
            print("contact not found")
    elif choice == 3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("enter the contact name to be edited")
        if edit_contact in contact:
            phone = input("enter mobile number")
            contact[edit_contact]=phone
            print("contact updated\n")
            display_contact()
        else:
            print("name not found")
    elif choice == 5:
        del_contact = input("enter the contact to be deleted")
        if del_contact in contact:
            confirm = input("do you want to delete contact y/n?")
            if confirm=='y' or confirm == 'Y':
                contact.pop(del_contact)
            display_contact()
            print("deleted succesfull\n")
        else:
            print ("contact not found")
    else:
        break
