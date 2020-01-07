import sqlite3


class AddressBook(object):
    def __init__(self, filename):
        self.dbfilename = filename
        self.db = sqlite3.connect(self.dbfilename)
        c = self.db.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY AUTOINCREMENT,"
                  " name TEXT, number TEXT,address TEXT)")
        self.db.commit()

    def view_all(self):
        c = self.db.cursor()
        c.execute('SELECT * FROM book')
        contact = c.fetchall()
        c.close()
        return contact

    def add_contact(self):
        name = input("Enter the name")
        phone_number = input("Enter the phone number ")
        address = input("Enter the address")
        c = self.db.cursor()
        c.execute('INSERT INTO book(name, number, address) VALUES (?,?,?)', (name, phone_number, address))
        self.db.commit()
        c.close()

    def delete_contact(self):
        user_input = input("Enter the user's name ")
        c = self.db.cursor()
        c.execute('DELETE FROM book WHERE name=?', (user_input,))
        self.db.commit()
        c.close()

    def view_contact(self):
        user_input = input("Enter the user's name")
        c = self.db.cursor()
        c.execute('SELECT * FROM book WHERE name=?', (user_input,))
        contact = c.fetchall()
        c.close()
        return contact

    def edit_contact(self):
        name = input("Enter the name")
        phone_number = input("Enter the phone number ")
        address = input("Enter the address")
        c = self.db.cursor()
        c.execute('UPDATE book set number=?, address=? WHERE name=?', (phone_number, address, name))
        self.db.commit()
        c.close()


ab = AddressBook(filename='addressbook.db')

while True:
    user_answer = input("Enter 1 to create a new contact, 2 to view a contact, 3 to edit a contact,"
                        "4 to delete a contact, 5 to view all contacts and 6 to come back later ")

    if user_answer == "1":
        ab.add_contact()

    elif user_answer == "2":
        print(ab.view_contact())

    elif user_answer == "3":
        ab.edit_contact()

    elif user_answer == "4":
        ab.delete_contact()

    elif user_answer == "5":
        view_all = ab.view_all()
        for row in view_all:
            print(row)
    else:
        print("Come back next time!")
        break
