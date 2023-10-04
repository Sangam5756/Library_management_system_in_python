
fd =open("lms.text",'a')  #open file in append mode

def add_book():# it is function to add books
    title = input("Enter the title of the book: ")
    author = input("\nEnter the author of the book: ")
    fd.write(title)
    fd.write("\n")
    fd.write(author)
    fd.write("\n")

   
fd_ =open("lms.text",'r')  #open file to read data

def view_books():        #Function to view the book
    print(fd_.read())
    fd_.close() #close the file after reading
    
   

while True:
    print("\nLibrary Management System Option:")
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

fd.close() # close the file after program execution
