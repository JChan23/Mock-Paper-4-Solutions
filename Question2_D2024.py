class Member:
    #self.__MemberID : STRING
    #self.__Name : STRING
    #self.__NumBorrowedItems : INTEGER
    #self.__BorrowedItems : DICTIONARY

    def __init__(self, ID, N):
        self.__MemberID = ID
        self.__Name = N
        self.__NumBorrowedItems = 0
        self.__BorrowedItems = {}

    def GetName(self):
        return self.__Name

    def GetInfo(self):
        info = "Name: "+self.__Name+", Member ID: "+self.__MemberID
        return info

    def AddBorrowedItem(self, book, return_date):
        if self.__NumBorrowedItems >= 5:
            print("Maximum number of books borrowed. Please return one of your books before borrowing another.")
            return
        self.__BorrowedItems[book] = return_date
        self.__NumBorrowedItems = self.__NumBorrowedItems + 1

    def RemoveBowwoedItem(self, book):
        if book not in self.__BorrowedItems.keys():
            print("Book was not borrowed by member.")
            return
        self.__BorrowedItems.pop(book)
        self.__NumBorrowedItems = self.__NumBorrowedItems - 1

    def OutputBorrowedItems(self):
        print(f"Borrowed items for {self.__Name}")
        for book, return_date in self.__BorrowedItems.items():
            print(f"{book}: {return_date}")


class Librarian(Member):
    #self.__Rank : STRING
    #self.__Salary : REAL

    def __init__(self, ID, N, R):
        Member.__init__(self, ID, N)
        self.__Rank = R
        if self.__Rank == "trainee":
            self.__Salary = 900.0
        elif self.__Rank == "assistant":
            self.__Salary = 1200.0
        elif self.__Rank == "junior":
            self.__Salary = 1800.0
        elif self.__Rank == "senior":
            self.__Salary = 2500.0
        else:
            print("Invalid rank")
            self.__Salary = None

    def SetRank(self, rank):
        self.__Rank = rank
        if self.__Rank == "trainee":
            self.__Salary = 900.0
        elif self.__Rank == "assistant":
            self.__Salary = 1200.0
        elif self.__Rank == "junior":
            self.__Salary = 1800.0
        elif self.__Rank == "senior":
            self.__Salary = 2500.0
        else:
            print("Invalid rank")
            self.__Salary = None

    def GetLibrarianInfo(self):
        info = Librarian.GetInfo(self)+", Rank: "+self.__Rank+", Salary: "+str(self.__Salary)
        return info

class Node:
    #self.__data : Librarian or Member
    #self.__right : Node
    #self.__left : Node

    def __init__(self, D):
        self.__data = D
        self.__right = None
        self.__left = None

    def Insert(self, person):
        if person.GetName() < self.__data.GetName():
            if self.__left is None:  # doesn't point to another node
                self.__left = Node(person)
                return
            else:
                self.__left.Insert(person)
        elif person.GetName() > self.__data.GetName():
            if self.__right is None:  # doesn't point to another node
                self.__right = Node(person)
                return
            else:
                self.__right.Insert(person)

    def PrintTree(self):
        if self.__left:  # is not None (i.e. node points to another node)
            self.__left.PrintTree()
        if type(self.__data) is Librarian:
            print(self.__data.GetLibrarianInfo())
        else:
            print(self.__data.GetInfo())
        if self.__right:  # is not None (i.e. node points to another node)
            self.__right.PrintTree()

    def Search(self, Name):
        if Name == self.__data.GetName():
            return self.__data
        elif Name < self.__data.GetName():
            if self.__left:  # is not None (i.e. node points to another node)
                return self.__left.Search(Name)
            else:
                return str(Name) + " was not found in the binary tree"
        elif Name > self.__data.GetName():
            if self.__right:  # is not None (i.e. node points to another node)
                return self.__right.Search(Name)
            else:
                return str(Name) + " was not found in the binary tree"


member = True #BOOLEAN
count = 1 #INTEGER
TreeStart = False #BOOLEAN
try:
    with open('library.txt') as file:
        for line in file:
            line = line.strip()
            if line == "Member":
                member = True
            elif line == "Librarian":
                member = False
            elif count == 2:
                MemberID = line
            elif count == 3:
                name = line
                if member == True:
                    if TreeStart == False:
                        BinaryTree = Node(Member(MemberID, name)) #TYPE Node
                        TreeStart = True
                    else:
                        BinaryTree.Insert(Member(MemberID, name))
            elif count == 4 and member == False:
                Rank = line
                if TreeStart == False:
                    BinaryTree = Node(Librarian(MemberID, name, Rank)) #TYPE Node
                    TreeStart = True
                else:
                    BinaryTree.Insert(Librarian(MemberID, name, Rank))
            elif line == "":
                count = 0
            else:
                split = line.split(", ")
                Book = split[0]
                Return_Date = split[1]
                BinaryTree.Search(name).AddBorrowedItem(Book, Return_Date)
            count = count + 1
except OSError:
    print("Sorry, could not find the file")

BinaryTree.PrintTree()

James = BinaryTree.Search("James")
James.SetRank("assistant")
James.RemoveBowwoedItem("Great Expectations")
James.AddBorrowedItem("Little Women", "2025-01-07")
James.AddBorrowedItem("The Scarlet Letter", "2025-01-14")
James.AddBorrowedItem("Rebecca", "2025-01-07")
James.AddBorrowedItem("The Grapes of Wrath", "2025-01-22")
James.AddBorrowedItem("Don Quixote", "2025-01-25")
print(James.GetLibrarianInfo())
James.OutputBorrowedItems()
