class Publisher:
    def title(self,name):
        print("Enter the name of book: ",name)

class Book(Publisher):
    def member(self,page_no):
        print("Enter the totla page number of book: ",page_no)

class Tape(Publisher):
    def time(self,play):
        print("Enter the total playing hour of tape: ",play)

b = Book()
t = Tape()
b.title("3 idiots")
b.member(630)
t.time("2.56 hrs")
