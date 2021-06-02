class Arith:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print("Addition of two number is: ",(self.a+self.b))

    def sub(self):
        print("Subtraction of two number is: ",(self.a-self.b))

    def mul(self):
        print("Multiplication of two number is: ",(self.a*self.b))

ar = Arith(45,10)
ar.add()
ar.sub()
ar.mul()