from math import *

class Cal2:
    def setdata(self,r):
        self.r = r

    def display(self):
        print("Area of Circle is = ",(self.r*self.r))

calc = Cal2()
calc.setdata(7)
calc.display()