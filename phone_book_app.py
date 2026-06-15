class Contact:
    phone_directory = []

    def __init__(self, name, phone_number):
        self.name, self.phone = name, phone_number
        Contact.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}, Contact number: {self.phone}"

    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_directory) == 0:
            print("No contacts found in the directory!")
        else:
            print("\nAll Contacts from directory: ")
            for contact in cls.phone_directory:
                print(contact.show_contact())

    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                print(contact.show_contact())
                return None

        print(f"No Contact found for {search_name}.")
        return None

    @classmethod
    def update_contact_phone_number(cls, u_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == u_name.lower():
                u_phone = input("Enter phone number: ")

                if Contact.validate_phone_number(u_phone):
                    contact.phone = u_phone
                    print("\nUpdated Contact:")
                    print(contact.show_contact())
                    return None

                else:
                    print(
                        f"Invalid phone number, phone number should be at least 8 digits and should only contains numbers.")
                    u_phone = input("Enter phone number: ")

                    if Contact.validate_phone_number(u_phone):
                        contact.phone = u_phone
                        print("\nUpdated Contact:")
                        print(contact.show_contact())
                        return None

        print(f"No Contact found for {u_name}")
        return None

    @classmethod
    def update_contact_name(cls, u_phone):
        for contact in cls.phone_directory:

            if contact.phone == u_phone:
                u_name = input("Enter name: ")
                contact.name = u_name
                print("\nUpdated Contact:")
                print(contact.show_contact())
                return None

        print(f"No Contact found for {u_phone}")
        return None

    @staticmethod
    def validate_phone_number(number):
        if len(number) >= 8 and number.isdigit():
            return True
        return False

print("Welcome to Contact Directory Management System:")

while True:
    print("\n"
          "1. Add Contacts\n"
          "2. Search Contact\n"
          "3. View All Contacts\n"
          "4. Update Contact\n"
          "5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n_contacts = int(input("\nHow many contacts do you want to add? "))
        for i in range(n_contacts):
            print(f"\nEnter details for {i + 1} contact:")
            name = input("Enter your name: ")
            phone_number = input("Enter phone number: ")

            if Contact.validate_phone_number(phone_number):
                Contact(name, phone_number)

            else:
                print(
                    f"Invalid phone number for {name}, phone number should be atleast 8 digits and should only contains numbers.")
                phone_number = input("Enter phone number: ")

                if Contact.validate_phone_number(phone_number):
                    Contact(name, phone_number)

    elif choice == 2:
        search_name = input("\nEnter name to be searched: ")
        Contact.search_contact(search_name)

    elif choice == 3:
        Contact.show_all_contacts()

    elif choice == 4:
        update = input("\nEnter name if you want to update phone number or enter phone number if you want to update name: ")
        if Contact.validate_phone_number(update):
            Contact.update_contact_name(update)

        else:
            Contact.update_contact_phone_number(update)

    elif choice == 5:
        break

    else:
        print("\nInvalid Input!!")
