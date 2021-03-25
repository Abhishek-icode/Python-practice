class liabrary():
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.landict = {}

    def displaybook(self):
        print(f"Welcome to Abhishek's liabrary We have books:---")
        for books in self.booklist:
            print(books)

    def landbook(self, user, book):
        if book not in self.landict.keys():
            self.landict.update({book:user})
            print(f"landbook database has boon updated. you can take this book now")
        else:
            print(f"book is allrady used by {self.landict[book]}")

    def addbook(self, book):
        self.booklist.append(book)
        print(f"book has been added the book list")

    def returnbook(self, book):
        self.landict.pop(book)

if __name__ == '__main__':
    alex = liabrary(["python", "php", "cpp", "java", "ml"], "Alexthink")

while(True):
    print(f"Welcome to the {alex.name} Library. Enter your choice to continue")
    print("1 - Display books")
    print("2 - land a books")
    print("3 - add a books")
    print("4 - return a books")

    user_inp = input()
    if user_inp not in ['1', '2', '3', '4']:
        print("pl")
        continue
    else:
        user_inp = int(user_inp)

    if user_inp == 1:
        alex.displaybook()

    elif user_inp == 2:
        user = input("Enter your name")
        book = input("Enter book's name do you want")
        alex.landbook(user, book)

    elif user_inp == 3:
        book = input("Enter the name of book you want to add")
        alex.addbook(book)

    elif user_inp == 4:
        book = input("enter the name of book you want to return")
        alex.returnbook(book)

    else:
        print("Not a valid option")

    print("Press q to quit and Press c to continue")
    user_inp2 = " "
    while(user_inp2!="q" and user_inp2!="c"):
        user_inp2 = input()
        if user_inp2 == "q":
            exit()
        elif user_inp2 == "c":
            continue
        else:
            print("You Entered Wrong key")