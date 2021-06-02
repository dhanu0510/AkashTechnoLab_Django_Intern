from math import *

class Cal3:
    def calInterest(self,p,r,t):
        self.p = p
        self.r = r
        self.t = t

    def display(self):
        print("Simple Interest(S.I) = ",(self.p*self.r*self.t)) #P = Principle(4500), R = rate(9.5% = 0.095), T = time(6 yrs)

calc = Cal3()
calc.calInterest(4500,0.095,6)
calc.display()