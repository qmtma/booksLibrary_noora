bookslist = []
readFile =open("books.txt","r")
next(readFile)
for i in readFile:
        i=i.split(';')
        bookslist.append(i)
readFile.close()
def display_book_details(BS_Code):
    readFile =open("books.txt","r")
    for i in readFile:
        i=i.split(';')
        if i[0] == BS_Code:
            print(" Title: ",i[1],"\n"
                  " Author: ",i[2],' \n'
                  " Series_Title: ",i[3],' \n'
                  " Copyright_Year: ",i[4],' \n'
                  " Publisher: ", i[5],' \n'
                  " Copies: ",i[6],' \n'
                  " Price: ",i[7],' \n')

def Display_books_by_publisher(publisher):
    publisherbooks=[]
    for i in bookslist:
        if publisher in i[5]:
            publisherbooks.append(i[1])
    print("Publisher Books are: ", publisherbooks)


def Display_books_by_author(author):
    authorbooks = []
    for i in bookslist:
        if author in i[2]:
            authorbooks.append(i[1])
    print("Publisher Books are: ", authorbooks)


def get_Total_stock_value():
    total_value = 0
    readFile = open("books.txt", "r")
    next(readFile)
    for i in readFile:
        i = i.split(';')
        total_value += int(i[6]) * int(i[7])
    readFile.close()
    print("Total Stock Price is: ", total_value," QR\n")


while (1):
    print("                 BookShope Application\n"
          "                    [5] Display details of a book\n"
          "                    [6] Display books by a given Publisher\n"
          "                    [8] Display books by a given Author\n"
          "                    [9] Display the Value of all books\n"
          "                    [0] Exit ")
    choice = input("Enter your Choice:  ")
    if choice == '5':
        BS_code = input("Please Enter the BS_Code of the book you are looking to get the details for: ")
        print("\n")
        display_book_details(BS_code)
    if choice == '6':
        publisher = input("Please Enter Publisher whom you seek its books: ")
        Display_books_by_publisher(publisher)
    if choice == '8':
        author = input("Please Enter Author whom you seek its books: ")
        Display_books_by_author(author)
    if choice == "9":
        get_Total_stock_value()
    if choice == "0":
        break
        
