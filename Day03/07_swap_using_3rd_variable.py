x , y = input("Enter two no:").split(' ')

x = int(x)
y = int(y)

print("-----------before swap--------")
print("x:",x)
print("y:",y)

temp = x
x = y
y = temp

print("-----------after swap--------")
print("x:",x)
print("y:",y)