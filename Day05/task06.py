from math import *

class Cal5:
    def __init__(self,w,l):
        self.w = w
        self.l = l

    def calArea(self):
         a = self.w*self.l

    def display(self):
        print("Area of Rectangle is: ",self.w*self.l)

calc = Cal5(7,8)
calc.display()