class ContactBook:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.is_available = True

class contacts:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"ContactBook '{book.name}' added to the contact.")


    def display_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            print("\nAvailable Books:")
            for book in available_books:
                 print(f"Contact Name: {book.name}, Number: {book.phone_number}, email: {book.email}")
        else:
            print("\n No Contacts are currently available in the List.")
           

    def search(self, name1):
        for book in self.books:
            if book.name == name:
                if not book.is_available:
                    book.is_available = False
                    print(f"Remove'{book.name}'")
                else:
                    print(f"Contact Name: {book.name}, Number: {book.phone_number}, email: {book.email}")
                return
        print("List not Found")

    def remove(self,con_name):
        for book_names in self.books:
            
          if book_names.name ==con_name:
            self.books.remove(book_names)
            print( name, " Contact is Removed")

    def exit():

        print("Good bye")
        exit()

        
        

           


      
       

        



   

# User interface code
library = contacts()

while True:
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name : ")
        phone_number = input("Enter phone_number : ")
        email = input("Enter Email : ")
        new_book = ContactBook(name, phone_number, email)
        library.add_book(new_book)

    elif choice == "2":
        library.display_available_books()

    elif choice=="3":
        name = input("Enter search contact  : ")
        library.search(name)

    elif choice=="4":
       name=input("Enter del Name ")
       library.remove(name)

    elif choice=="5":
         print("Good bye")
         break

   


    else:
        print("Invalid choice. Please select a valid option.")

    