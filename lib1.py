# we will store all books in our library in the following list.
books = []

# This function adds a new book into our library
def addBook():
    bookName = input('Enter book name: ')
    bookAuthor = input('Enter book author name: ')
    # book[0] = Book ID
    # book[1] = Book Name
    # book[2] = Book Author
    # book[3] = User name to whom book is issued
    book = [len(books) + 1, bookName, bookAuthor, '']
    books.append(book)
    print("\nBook added successfully")

# This function will delete a book from our library
def deleteBook():
    bookId = int(input('\nEnter ID of book to be deleted: '))
    idx = 0
    bookDeleted = False
    while idx < len(books):
        if books[idx][0] == bookId:
            print("Found book. Book ID: {}, Book name: {}, Book author: {}, Issued to: {}".format(books[idx][0], books[idx][1], books[idx][2], books[idx][3]))
            del books[idx]
            print("Book with ID: {} successfully deleted".format(bookId))
            bookDeleted = True
            break
        idx = idx + 1
    if bookDeleted == False:
        print("Invalid book ID. There is no book with ID: {}".format(bookId))

# This function lists all the books in our library
def listBooks():
    print('\nListing all books in library\n')
    if len(books) == 0:
        print("There are no books in the library")
    else:
        for book in books:
            print("Book ID: {}, name: {}, author: {}, Issued to: {}".format(book[0], book[1], book[2], book[3]))

# This function will issue a book to a user
def issueBook():
    bookFound = False

    bookId = int(input("Enter book ID to issue: "))
    for book in books:
        if book[0] == bookId:
            bookFound = True
            if len(book[3]) > 0:
                print("\nCannot issue as book with ID: {} is already issued to user: {}".format(bookId, book[3]))
                break
            else:
                userName = input("Enter name of user to whom to issue this book: ")
                book[3] = userName
                print("Book with ID: {} issued to user name: {}".format(bookId, userName))

    if bookFound == False:
        print('No book found with ID: {}'.format(bookId))
# This function is used to return a book to the library
def returnBook():
    bookFound = False

    bookId = int(input("Enter book ID to return: "))

    for book in books:
        if book[0] == bookId:
            bookFound = True
            if len(book[3]) > 0:
                userName = book[3]
                book[3] = ''
                print('Book with ID: {} has been unassigned from username: {}'.format(bookId, userName))
            else:
                print('Book with ID: {} is not assigned to any user'.format(bookId))
    if bookFound == False:
        print('No book found with ID: {}'.format(bookId))


response = ''

while response != 0:
    print("\n\n    LIBRARY MENU    \n")
    print("1. Add book")
    print("2. Delete book")
    print("3. List books")
    print("4. Issue book")
    print("5. Return book")
    print("0. Exit")
    response = input("\nChoose an option [0-5]: ")
    if response not in ('1', '2', '3', '4', '5', '0'):
        print("\nInvalid response. Please try again")
    else:
        response = int(response)
        if response == 1:
            addBook()
        elif response == 2:
            deleteBook()
        elif response == 3:
            listBooks()
        elif response == 4:
            issueBook()
        elif response == 5:
            returnBook()
        elif response == 0:
            print('\nThank you for using library management system. Bye...')

