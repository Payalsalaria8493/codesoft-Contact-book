contact = {}

def display_contact():
    print("Name\t\tContact number ")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
    
print("Welcome to Contact Book\n\nPlease Enter Your Name : ")
username = input("Enter your name : ")
print("Hello " + username)
while True:
    
    choice = int(input("1.Add new contact \n2.Search contact  \n3.Display contact \n4.Edit contact \n5.Delete contact \n6. Exit \nEnter your choice : "))
    if choice ==1:
        Name =input("Enter Name : ")
        phone = input("Enter mobile number : ")
        contact.update({Name:phone})
    elif choice ==2:
        search_name = input("Enter the contact name : ")
        if search_name in contact:
            #  print(f"{search_name}'s contact number is {contact[search_name]}")
            print(f"{search_name}\t\t{contact[search_name]}")
        else:
            print("Contact not Found....")
    elif choice ==3:
        if not contact:
            print("Empty contact book..")
        else:
            display_contact()
    elif choice==4:
        edit_contact = input("Enter contact to be edit : ")
        if edit_contact in contact:
            phone = int(input("Enter phone number : "))
            contact[edit_contact]=phone
        else:
            print("Name is not found in the book")
    elif choice ==5:
        del_contact = input("Enter contact to be delete : ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n? ")
            if confirm == "y" or confirm == "Y":
                contact.pop(del_contact)
                display_contact()
    else:
        break







