class Scheme:
    def scheme_id(self,id):
        print("Enter your scheme id: ",id)

    def scheme_name(selfself,sname):
        print("Enter scheme name: ",sname)

    def outing_rate(self,rate):
        print("Enter rate of outgoing: ",rate)

    def message_charge(self,msg):
        print("Enter charge of messages: ",msg)

class Customer(Scheme):
    def cust_id(self,id1):
        print("Enter customer's id: ",id1)

    def cust_name(selfself,name):
        print("Enter customer's name: ",name)

    def mobile_no(self,num):
        print("Enter customer's mobile number: ",num)

cust = Customer()
cust.scheme_id(2)
cust.scheme_name("Binge all night with weekend data roll over at rs. 699")
cust.outing_rate(0)
cust.message_charge(0)
cust.cust_id(123)
cust.cust_name("Dhananjay Patel")
cust.mobile_no(8154995870)