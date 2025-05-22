def main():
    try:
        # initialize the book list 
        booklist = []
        infile = open("booklist.txt", "r")
        line = infile.readline()
        while line:
            # Fix: First strip newline, then split by comma
            items = line.strip().split(",")
            if len(items) == 3:  # Ensure we have all three pieces of data
                nBook, nAuthor, nPages = items
                booklist.append([nBook, nAuthor, int(nPages)])
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("File not found, creating a new book list")
        print("starting with an empty book list")
        booklist = []


    choice = 0
    while choice != 4:
        print("***Books manager***")
        print("1.Add a book")
        print("2.Look up for a book")
        print("3.Display a book")
        print("4.Quit")
        choice = int(input("Enter your choice:"))

        if choice == 1:
            print("Adding a book")
            nBook = input("Enter the name of the book:")
            nAuthor = input("Enter the author of the book:")
            nPages = int(input("Enter the number of pages:"))
            booklist.append([nBook, nAuthor, nPages])
            print("Book added successfully")
        elif choice == 2:
            print("Looking up for a book ")
            keywoard = input("Enter the search term:")
            for book in booklist:
                if keywoard in book:
                    print("Book found")
        elif choice == 3:
            print("Dipslaying a book")
            for i in range(len(booklist)):
                print(booklist[i])
        elif choice == 4:
            print("Quitting the program")
            print("Program terminated")

        # saving to external Txt file 
        outfile = open("booklist.txt", "w")  # Fixed typo in filename (was boooklist.txt)
        for book in booklist:
            # Convert all elements to strings before joining
            book_str = [str(item) for item in book]
            outfile.write(",".join(book_str) + "\n")
        outfile.close()
if __name__ == "__main__":
    main()