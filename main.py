
print("-----------------------")
print("| Connect with CTACT  |")
print("-----------------------")

ux = True
while ux:
    user_choice = input(
        "\nEnter 'V' to view contacts, 'D' to delete or 'A' to add or 'E' to exit: ").upper()

    if user_choice == 'V':
        with open("data.txt", 'r') as data:
            contact = data.read()
            print(contact)

    elif user_choice == 'A':
        with open('data.txt', 'a') as data:
            firstname = input("\nFirst name of your contact: ").capitalize()
            lastname = input("Last name of your contact: ").capitalize()
            phonenumber = input(
                "Enter the phone number digits in this format 'xxxxxxxxxx': ")

            data.write(
                f"\n{firstname} {lastname} ({phonenumber[0:3]}) {phonenumber[3:6]}-{phonenumber[6:10]}")

    elif user_choice == 'D':
        with open('data.txt', 'r') as data:
            lines = data.readlines()
            name = input(
                "Enter the first name of the contact you want to delete: ").upper()

        with open("data.txt", "w") as f:
            for line in lines:
                n = (line.strip("\n")[0:4])
                if n.upper() == name[0:4]:
                    deleted = [line]
                    print(f"\nDeleted: {deleted[0]}")

                else:
                    f.write(line)

    else:
        print("\n\nThanks for stopping by!")
        ux = False
