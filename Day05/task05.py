class Employee:
    def info(self,name,designation):
        print("Employee's name: ",name)
        print("Employee's designation: ",designation)

class Sal(Employee):
    def salary(self,salary):
        print("Salary is: ",salary)

s = Sal()
s.info("Dhananjay Patel","Python Developer")
s.salary(50000)

