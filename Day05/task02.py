from math import *

class Cal2:
    def setdata(self,r):
        self.r = r

    def area(self):
        print("Area of Circle is = ",(pi*self.r*self.r))

calc = Cal2()
calc.setdata(7)
calc.area()