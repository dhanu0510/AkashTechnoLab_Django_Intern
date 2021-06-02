from math import *

class Cal6:
    def setdata(self):
        self.l = int(input("Entrer the length of square: "))

    def area(self):
         return self.l*self.l

    def display(self):
        print("Area of Square is: ",a)

calc = Cal6()
calc.setdata()
a = calc.area()
calc.display()