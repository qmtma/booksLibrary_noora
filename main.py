bookslist = [] # creating an empty list to store all books details in an iterable easily processed object 
readFile =open("books.txt","r") # opening book.txt in read mode
next(readFile) # skip first line of the txt file due to redundancy an irrelevancy 
for i in readFile: # looping through the lines to start manipulating them and store them in booklist LIST 
        i=i.split(';') # removing the delimiter from the lines
        bookslist.append(i) # append each line in booklist LIST creating a LIST of LIST
readFile.close() # close the file ( coding convention to save resources and potential errors)

def display_book_details(BS_Code): # function declaration taking BS_Code as an argument 
    readFile =open("books.txt","r") # open file for reading
    next(readFile)
    for i in readFile:
        i=i.split(';')
        if i[0] == BS_Code: # conditional logic to find the BS_Code requested by the user in the Library i[0] is the
                            # index of the BS_code in the File
            print(" Title: ",i[1],"\n" # print function will display all details stored for the found book next to the
                  " Author: ",i[2],' \n' # relevant description 
                  " Series_Title: ",i[3],' \n'
                  " Copyright_Year: ",i[4],' \n'
                  " Publisher: ", i[5],' \n'
                  " Copies: ",i[6],' \n'
                  " Price: ",i[7],' \n')

def Display_books_by_publisher(publisher): # function declaration to display books per publisher taking the publisher as function argument
    publisherbooks=[] # empty list to store found books of the desired publisher
    for i in bookslist:
        if publisher in i[5]: # if the publisher name requested by the user is found partially in the publisher field
            publisherbooks.append(i[1]) # append found book title to the publisherbooks LIST
    print("Publisher Books are: ", publisherbooks) # print found LIST


def Display_books_by_author(author): # function declaration to display books found per author taking the auther name as an argument
    authorbooks = [] # empty list to store found books of the desired author
    for i in bookslist:
        if author in i[2]: # if the author name requested by the user is found partially in the author field
            authorbooks.append(i[1]) # append found books to the publisherbooks LIST
    print("Publisher Books are: ", authorbooks) # print found books titles


def get_Total_stock_value(): # function declaration computing total stock value of the library
    total_value = 0 # initializing total_calue integer
    readFile = open("books.txt", "r")
    next(readFile)
    for i in readFile:
        i = i.split(';')
        total_value += int(i[6]) * int(i[7]) # multiply book cost * book copies and add it to the total value
        # this function excutes per line computing total price of each book stock and add it to the total_value
    readFile.close()
    print("Total Stock Price is: ", total_value," QR\n") # print results


while (1): # infinite loop for the main menu of the application end when the user enters 0 as his choice of function
    
    print("                 BookShope Application\n" # display user options
          "                    [5] Display details of a book\n"
          "                    [6] Display books by a given Publisher\n"
          "                    [8] Display books by a given Author\n"
          "                    [9] Display the Value of all books\n"
          "                    [0] Exit ")
    choice = input("Enter your Choice as a number:  ") # ask the user to choose his required function
    if choice == '5': # if user enters 5 
        BS_code = input("Please Enter the BS_Code of the book you are looking to get the details for: ")
        print("\n") # visual space for easier reading of the next results
        display_book_details(BS_code) # function call to display book details 
    if choice == '6': # if user chooses 6 
        publisher = input("Please Enter Publisher whom you seek its books: ")
        Display_books_by_publisher(publisher) # function call displaying books per publisher
                                              # this function will display books even if the input is partially found
    if choice == '8': # if user chooses 8 
        author = input("Please Enter Author whom you seek its books: ")
        Display_books_by_author(author) # fuction call to display books per author
                                        # this function will display results even if the input is found partially in the author fielf
    if choice == "9": # if the user chooses 9 
        get_Total_stock_value() # function call to calculate total stock price
    if choice == "0": # if the user chooses 0 
        break # terminate the loop, closing the program
        
