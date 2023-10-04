fd =open("lms.text",'a')

def add_book():
    title = input("Enter the title of the book: ")
    author = input("\nEnter the author of the book: ")
    fd.write(title)
    fd.write("\n")
    fd.write(author)
    fd.write("\n")

   
fd_ =open("lms.text",'r')

def view_books():
    print(fd_.read())
    fd_.close()
    
   

while True:
    print("\nLibrary Management System Menu:")
    print("1. Add a book")
    print("2. View books")
    print("3. Exit")


    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

fd.close() 