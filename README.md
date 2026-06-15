# Contact Directory Management System

## Overview

The Contact Directory Management System is a Python-based console application that allows users to manage contacts efficiently. Users can add new contacts, search existing contacts, view all saved contacts, and update contact details such as name or phone number.

This project demonstrates the implementation of Object-Oriented Programming (OOP) concepts in Python, including classes, objects, class methods, static methods, and data validation.

---

## Features

### 1. Add Contacts

* Add one or multiple contacts.
* Store contact name and phone number.

### 2. Search Contact

* Search a contact using the contact name.
* Displays contact details if found.

### 3. View All Contacts

* Displays all contacts stored in the directory.

### 4. Update Contact Information

* Update a contact's phone number using their name.
* Update a contact's name using their phone number.

### 5. Phone Number Validation

* Phone number must contain only digits.
* Phone number must be at least 8 digits long.

### 6. Exit Application

* Safely exits the program.

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

---

## Project Structure

```
contact_directory.py
README.md
```

---

## OOP Concepts Used

### Class

`Contact`

Represents a contact in the phone directory.

### Constructor

```python
__init__()
```

Initializes contact name and phone number.

### Instance Method

```python
show_contact()
```

Returns the details of a single contact.

### Class Methods

```python
show_all_contacts()
search_contact()
update_contact_phone_number()
update_contact_name()
```

Operate on the shared phone directory.

### Static Method

```python
validate_phone_number()
```

Validates phone numbers without requiring class or object data.

---

## How to Run

### Step 1: Clone the Repository

```bash
git clone <repository-url>
```

### Step 2: Navigate to Project Folder

```bash
cd contact-directory-management-system
```

### Step 3: Run the Program

```bash
python contact_directory.py
```

---

## Sample Menu

```text
Welcome to Contact Directory Management System:

1. Add Contacts
2. Search Contact
3. View All Contacts
4. Update Contact
5. Exit
```

---

## Sample Output

```text
How many contacts do you want to add? 2

Enter details for 1 contact:
Enter your name: John
Enter phone number: 98765432

Enter details for 2 contact:
Enter your name: Alice
Enter phone number: 12345678

All Contacts from directory:
Name: John, Contact number: 98765432
Name: Alice, Contact number: 12345678
```

---

## Validation Rules

* Phone number must contain digits only.
* Phone number length must be at least 8 characters.

Example of invalid input:

```text
Phone Number: abc123
```

Example of valid input:

```text
Phone Number: 9876543210
```

---

## Future Enhancements

* Delete Contact Feature
* Duplicate Contact Detection
* Save Contacts to File
* Load Contacts from File
* Contact Sorting
* GUI Version using Tkinter
* Database Integration using SQLite/MySQL

---

## Learning Outcomes

After completing this project, students will understand:

* Classes and Objects
* Constructors
* Class Variables
* Class Methods
* Static Methods
* Data Validation
* Lists and Loops
* Menu-Driven Programming
* Object-Oriented Programming in Python

---

## Author

Developed as a Python Mini Project for learning Object-Oriented Programming concepts and Contact Management Systems.
