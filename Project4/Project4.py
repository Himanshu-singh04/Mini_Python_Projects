class Library:
    def __init__(self, listOfbooks):
        self.books = listOfbooks
    def displayAvailablebooks(self):
        print("Books in the library are: ")
        for books in self.books:
            print (books)
    
    def _borrow(self, bookName):
        if bookName in self.books:
            print(f"you have issued the book named {bookName}")
            self.books.remove(bookName)
            return True
        else:
            print("book has already being issued")
            return False
    def _return(self, bookName):
        self.books.append(bookName)
        print(f"thanks for returning the {bookName}")
class Student:
    def _request(self):
        self.req = input("enter the name of book")
        return self.book
    
    def _return(self):
        self.ret = input(f"you have returned the book")
        return self.book
if __name__=="__main__":
    l = Library(["Apple","Banana"])
    i = Student()
    # l.displayAvailablebooks()
    while (True):
            welcome = '''Welcome to the library
            1. List of all books
            2. request a book
            3. return a book
            4. exit library'''

            a = int(input("Enter the response"))
            if a == 1:
                l.displayAvailablebooks()
            elif a == 2:
                i._request()
            elif a == 3:
                i._return()
            elif a == 4:
                exit()
            else:
                print("you entered invalid number")

    
  
    
