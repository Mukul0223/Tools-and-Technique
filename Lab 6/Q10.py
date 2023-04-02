# Write a menu driven program that keeps records of books and journal available in a library.
class Library:
    def __init__(self):
        self.books = []
        self.journals = []
    
    def add_book(self, title, author):
        self.books.append({"Title": title, "Author": author})
    
    def add_journal(self, title, editor):
        self.journals.append({"Title": title, "Editor": editor})
    
    def print_books(self):
        print("Books:")
        for book in self.books:
            print(f"{book['Title']} by {book['Author']}")
    
    def print_journals(self):
        print("Journals:")
        for journal in self.journals:
            print(f"{journal['Title']} edited by {journal['Editor']}")

# Create a Library instance
library = Library()

# Loop until the user chooses to quit
while True:
    # Print the menu
    print("\nMenu:")
    print("1. Add book")
    print("2. Add journal")
    print("3. Print books")
    print("4. Print journals")
    print("5. Quit")
    
    # Prompt the user to enter a choice
    choice = input("Enter choice: ").strip()
    
    # Take action based on the user's choice
    if choice == "1":
        title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()
        library.add_book(title, author)
        print("Book added.")
    elif choice == "2":
        title = input("Enter journal title: ").strip()
        editor = input("Enter journal editor: ").strip()
        library.add_journal(title, editor)
        print("Journal added.")
    elif choice == "3":
        library.print_books()
    elif choice == "4":
        library.print_journals()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
