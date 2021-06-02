class Cal1:
    def setdata(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def display(self):
        print("Sum = ",self.a + self.b + self.c)

calc = Cal1()
calc.setdata(4,5,6)
calc.display()