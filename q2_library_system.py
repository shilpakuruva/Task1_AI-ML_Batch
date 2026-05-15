# Function to add a book
def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print(f"Book '{title}' added successfully.")


# Function to borrow a book
def borrow_book(catalog, borrowed_books, book_id):

    if book_id not in catalog:
        print("Book does not exist.")
        return

    if book_id in borrowed_books:
        print("Book is already borrowed.")
        return

    borrowed_books.append(book_id)
    print(f"Book ID {book_id} borrowed successfully.")


# Function to return a book
def return_book(borrowed_books, book_id):

    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book ID {book_id} returned successfully.")
    else:
        print("Book was not borrowed.")


# Function to register a member
def register_member(members, member_id):

    members.add(member_id)
    print(f"Member {member_id} registered.")


# Function to show available books
def show_available(catalog, borrowed_books):

    print("\nAvailable Books:")

    for book_id, details in catalog.items():

        if book_id not in borrowed_books:

            title, author, year = details

            print(f"{book_id} -> {title} | {author} | {year}")


# Main function
def main():

    # Data structures
    catalog = {}
    borrowed_books = []
    members = set()

    # Adding 4 books
    add_book(catalog, 101, "Python Basics", "John Smith", 2020)
    add_book(catalog, 102, "DBMS Concepts", "Ravi Kumar", 2019)
    add_book(catalog, 103, "Data Structures", "Alice Brown", 2021)
    add_book(catalog, 104, "Machine Learning", "Andrew Ng", 2022)

    print()

    # Registering members
    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)

    # Duplicate member
    register_member(members, 2)

    print("\nMembers:", members)

    print()

    # Borrowing books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    # Trying to borrow again
    borrow_book(catalog, borrowed_books, 101)

    print("\nBorrowed Books:", borrowed_books)

    print()

    # Returning one book
    return_book(borrowed_books, 101)

    print("\nBorrowed Books after return:", borrowed_books)

    # Show available books
    show_available(catalog, borrowed_books)


# Run program
main()
